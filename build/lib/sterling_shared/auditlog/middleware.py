
import datetime
import json
import logging
import re

import jwt

from django.utils.deprecation import MiddlewareMixin
from .auditlog_data import AuditLogData

class AuditLogMiddleware(MiddlewareMixin):
    PATH_TO_EXEMPT = [
            "/api/doc/",
            "/api/schema/",
            "/api/v1/doc/",
            "/api/v1/configs/current/",
            "/api/v1/auth/login/",
            "/api/v1/auth/token/refresh/",
            "/api/v1/auth/token/verify/",
            "/api/v1/auth/decode/",
            "/api/v1/auth/2FA/",
            "/api/v1/users/profile/",
            "/api/v1/auth/ad/login/",
            "/api/v1/auth/ad/redirect-url/",
        ]

    def get_log_pusher(self):
        """
        Should return a celery task function to be used to push log data
        For example: return my_log_pusher.delay
        """
        raise NotImplemented

    def get_module_name(self, request) -> str:
        raise NotImplemented

    def get_module_id(self, request) -> str:
        raise NotImplemented

    def extract_browser_name(self, user_agent):
        browser_patterns = {
            'Chrome': 'Chrome\/[\d.]+',
            'Firefox': 'Firefox\/[\d.]+',
            'Safari': 'Version\/[\d.]+.*Safari',
            'Edge': 'Edge\/[\d.]+',
            'IE': 'Trident\/[\d.]+',
            'Opera': 'Opera\/[\d.]+',
        }
        for browser_name, pattern in browser_patterns.items():
            match = re.search(pattern, user_agent)
            if match:
                return browser_name
        return '<UNKNOWN>'

    @classmethod
    def get_exempt_paths(cls):
        return cls.PATH_TO_EXEMPT or []
    
    def get_client_ip(self, request):
        """
        get client ip address
        """
        try:
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR', None)
            if ip_address:
                ip_address = ip_address.split(', ')[0]
            else:
                ip_address = request.META.get('REMOTE_ADDR', '')
            return ip_address
        except Exception as ex:
            print("AuditLogMiddleware.get_client_ip", ex)
            return "<UNKNOWN>"

    def process_request(self, request):
        exempt_paths = AuditLogMiddleware.get_exempt_paths()
        if (
                request.path not in exempt_paths
                and not request.path.startswith("/admin/")
                and "__debug__" not in request.path
        ) and request.headers.get("Authorization"):
            try:
                request.audit_data = AuditLogData()
                request.audit_data.sourceIP = self.get_client_ip(request)
                request.audit_data.ipAddress = self.get_client_ip(request)
                request.audit_data.location = self.get_client_ip(request)
                request.audit_data.clientInfo = self.extract_browser_name(
                    request.META.get('HTTP_USER_AGENT', ''))
                request.audit_data.module = self.get_module_name(request)
                request.audit_data.moduleID = self.get_module_id(request)
            except Exception as ex:
                import traceback
                print("sterling_shared.AuditLogMiddleware.process_request", ex)
                traceback.print_exc()

    def infer_activity_type(self, method, path):
        activity_type = "VIEW"
        if method in ("PUT", "PATCH", "UPDATE"):
            activity_type = "MODIFICATION"
        elif method == "POST":
            activity_type = "CREATION"
            if "change" in path or "update" in path or "edit" in path:
                activity_type = "MODIFICATION"
        elif method == "DELETE":
            activity_type = "DELETION"
        if "reject" in path:
            activity_type = "REJECTION"
        elif "approve" in path:
            activity_type = "APPROVAL"
        elif "deactivate" in path:
            activity_type = "DEACTIVATION"
        elif "reactivate" in path:
            activity_type = "REACTIVATION"
        elif "delete" in path:
            activity_type = "DELETION"
        if "check" in path:
            activity_type = "VIEW"
        if "withdraw" in path:
            activity_type = "WITHDRAWAL"
        return activity_type

    def process_response(self, request, response):
        exempt_paths = AuditLogMiddleware.get_exempt_paths()
        if (
                request.path not in exempt_paths
                and not request.path.startswith("/admin/")
                and "__debug__" not in request.path
        ) and request.headers.get("Authorization"):
            try:
                request.audit_data.userActivityType = \
                    self.infer_activity_type(request.method, request.path)
                request.audit_data.microserviceName = \
                    request.audit_data.microserviceName or \
                    request.resolver_match.view_name.split('.')[-1].replace(
                        "View", ""
                    )
                request.audit_data.endpointName = request.resolver_match.view_name
                request.audit_data.action = f"{request.audit_data.userActivityType} on {request.audit_data.microserviceName}"
                request.audit_data.endDate = str(datetime.datetime.now())
                is_success = response.status_code in range(200, 299)
                request.audit_data.actionStatus = "Successful" if is_success else "Failed"
                if not is_success:
                    request.audit_data.reasonForFailure = \
                        response.content.decode('utf-8')
                if request.user.is_authenticated:
                    user = request.user
                    request.audit_data.userID = str(user.id)
                    request.audit_data.lastLogin = str(user.last_login)
                    request.audit_data.userName = str(user.username or user.email)
                    request.audit_data.fullName = f"{user.firstname} {user.lastname}"
                    token_key = request.headers.get("Authorization").split(" ")[-1]
                    request.audit_data.sessionID = token_key
                    decoded_token = jwt.decode(
                        token_key, options={"verify_signature": False}
                    )
                    role_ids = ", ".join(str(role_id) for role_id in decoded_token.get(
                        "role_ids", ""))
                    role_names = ", ".join(
                        str(role_name) for role_name in decoded_token.get(
                            "role_names", ""
                        )
                    )
                    request.audit_data.roleId = role_ids
                    request.audit_data.roleName = role_names
                print("audit_data", request.audit_data.to_dict())
                self.get_log_pusher()(request.audit_data)
            except Exception as ex:
                import traceback
                print("sterling_shared.AuditLogMiddleware.process_response", ex)
                traceback.print_exc()
        return response
