import datetime
import uuid
import json


class AuditLogData:
    def __init__(self):
        now = str(datetime.datetime.now())
        self.auditID = str(uuid.uuid4())
        self.action = ""
        self.sourceIP = ""
        self.roleId = ""
        self.userActivityType = ""
        self.microserviceName = ""
        self.payloadCreatedDate = now
        self.endpointName = ""
        self.oldValuesJson = {}
        self.newValuesJson = {}
        self.affectedColumns = []
        self.role = ""
        self.userName = ""
        self.fullName = ""
        self.userID = ""
        self.createdDate = now
        self.ipAddress = ""
        self.startDate = now
        self.endDate = ""
        self.branchCode = ""
        self.location = ""
        self.branchName = ""
        self.clientInfo = ""
        self.actionStatus = ""
        self.lastLogin = ""
        self.sessionID = ""
        self.module = ""
        self.moduleID = ""
        self.timestamp = now
        self.productId = ""
        self.productType = ""
        self.productName = ""
        self.reasonForFailure = ""
        self.otherInformation = ""
        self.authorizationDetails = ""
        self.ledgerId = ""
        self.ledgerName = ""
        self.ledgerType = ""
        self.ledgerClass = ""
        self.customerId = ""
        self.customerType = ""
        self.customerName = ""
        self.journalEntryInformation = ""
        self.transactionValue = ""
        self.exchangeRate = ""
        self.debitAccounts = ""
        self.creditAccounts = ""
        self.chargeCode = ""
        self.chargeName = ""
        self.taxCode = ""
        self.taxName = ""
        self.recordId = ""
        self.recordName = ""
        self.transactionEntryInformation = ""
        self.customerMandateView = ""
        self.modifiedParameter = ""
        self.periodCode = ""
        self.currencyCode = ""
        self.auditModuleAccessed = ""
        self.investmentEntryInformation = ""
        self.investmentProduct = ""
        self.investmentAmount = ""
        self.debitAccountLedger = ""
        self.creditAccountLedger = ""
        self.loanEntryInformation = ""
        self.loanProduct = ""
        self.loanAmount = ""
        self.eocRunInformation = ""
        self.eocRunLog = ""

    def guess_affected_cols(self):
        if self.affectedColumns:
            return self.affectedColumns
        cols = []
        if isinstance(self.newValuesJson, dict):
            for k in self.newValuesJson:
                if self.oldValuesJson.get(k) != self.newValuesJson[k]:
                    cols.append(k)
        if 'password' in self.newValuesJson:
            self.newValuesJson['password'] = "***"
        if 'password' in self.oldValuesJson:
            self.oldValuesJson['password'] = "***"
        return cols

    def to_dict(self):
        from .utils import jsonize

        # return 
        res = {
            "auditID": self.auditID,
            "action": self.action,
            "sourceIP": self.sourceIP,
            "roleId": self.roleId,
            "userActivityType": self.userActivityType,
            "microserviceName": self.microserviceName,
            "payloadCreatedDate": self.payloadCreatedDate,
            "endpointName": self.endpointName,
            "oldValuesJson": jsonize(self.oldValuesJson),
            "newValuesJson": jsonize(self.newValuesJson),
            "affectedColumns": jsonize(self.guess_affected_cols()),
            "role": self.role,
            "userName": self.userName,
            "fullName": self.fullName,
            "userID": self.userID,
            "createdDate": self.createdDate,
            "ipAddress": self.ipAddress,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "branchCode": self.branchCode,
            "location": self.location,
            "branchName": self.branchName,
            "clientInfo": self.clientInfo,
            "actionStatus": self.actionStatus,
            "lastLogin": self.lastLogin,
            "sessionID": str(self.sessionID),
            "module": self.module,
            "moduleID": self.moduleID,
            "timestamp": self.timestamp,
            "productId": self.productId,
            "productType": self.productType,
            "productName": self.productName,
            "reasonForFailure": self.reasonForFailure,
            "otherInformation": self.otherInformation,
            "authorizationDetails": self.authorizationDetails,
            "ledgerId": self.ledgerId,
            "ledgerName": self.ledgerName,
            "ledgerType": self.ledgerType,
            "ledgerClass": self.ledgerClass,
            "customerId": self.customerId,
            "customerType": self.customerType,
            "customerName": self.customerName,
            "journalEntryInformation": self.journalEntryInformation,
            "transactionValue": self.transactionValue,
            "exchangeRate": self.exchangeRate,
            "debitAccounts": self.debitAccounts,
            "creditAccounts": self.creditAccounts,
            "chargeCode": self.chargeCode,
            "chargeName": self.chargeName,
            "taxCode": self.taxCode,
            "taxName": self.taxName,
            "recordId": self.recordId,
            "recordName": self.recordName,
            "transactionEntryInformation": self.transactionEntryInformation,
            "customerMandateView": self.customerMandateView,
            "modifiedParameter": self.modifiedParameter,
            "periodCode": self.periodCode,
            "currencyCode": self.currencyCode,
            "auditModuleAccessed": self.auditModuleAccessed,
            "investmentEntryInformation": self.investmentEntryInformation,
            "investmentProduct": self.investmentProduct,
            "investmentAmount": self.investmentAmount,
            "debitAccountLedger": self.debitAccountLedger,
            "creditAccountLedger": self.creditAccountLedger,
            "loanEntryInformation": self.loanEntryInformation,
            "loanProduct": self.loanProduct,
            "loanAmount": self.loanAmount,
            "eocRunInformation": self.eocRunInformation,
            "eocRunLog": self.eocRunLog
        }
        
        json_res = json.dumps(res)
        print("Serialized JSON:", json_res)
        print("OLD Values after serialization:", res["oldValuesJson"])
        print("NEW Values after serialization:", res["newValuesJson"])
        resss = json.loads(json_res)
        old_value = resss["oldValuesJson"]
        new_value = resss["newValuesJson"]
        clean_old_value = json.loads(old_value)
        clean_new_value = json.loads(new_value)
        resss["oldValuesJson"] = clean_old_value
        resss["newValuesJson"] = clean_new_value

        print("we are sending:", resss, "________________________")
        return resss
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return json.dumps(self.to_dict())
    
    def __unicode__(self):
        return self.__str__()
    
