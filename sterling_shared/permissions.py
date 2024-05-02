from dataclasses import dataclass


@dataclass
class PERMISSIONS:
    # User permissions
    APPROVE_USER_REQUEST = "APPROVE_USER_REQUEST"
    APPROVE_USERS = "APPROVE_USERS"
    CREATE_USER = "CREATE_USER"
    DISABLE_USER = "DISABLE_USER"
    ENABLE_USER = "ENABLE_USER"
    LIST_USERS = "LIST_USERS"
    MODIFY_USER = "MODIFY_USER"
    VIEW_USER_DETAILS = "VIEW_USER_DETAILS"

    # Role permissions
    APPROVE_ROLE_REQUEST = "APPROVE_ROLE_REQUEST"
    CREATE_ROLE = "CREATE_ROLE"
    DISABLE_ROLE = "DISABLE_ROLE"
    ENABLE_ROLE = "ENABLE_ROLE"
    LIST_ROLES = "LIST_ROLES"
    MODIFY_ROLE = "MODIFY_ROLE"
    VIEW_ROLE_DETAILS = "VIEW_ROLE_DETAILS"

    # Config engine permissions
    MANAGE_SOD_CONFIG = "MANAGE_SOD_CONFIG"
    MANAGE_SECURITY_CONFIG = "MANAGE_SECURITY_CONFIG"

    # Fiscal Period permissions
    APPROVE_FISCAL_PERIOD_REQUEST = "APPROVE_FISCAL_PERIOD_REQUEST"
    CREATE_FISCAL_PERIOD = "CREATE_FISCAL_PERIOD"
    DISABLE_FISCAL_PERIOD = "DISABLE_FISCAL_PERIOD"
    ENABLE_FISCAL_PERIOD = "ENABLE_FISCAL_PERIOD"
    LIST_FISCAL_PERIOD = "LIST_FISCAL_PERIOD"
    MODIFY_FISCAL_PERIOD = "MODIFY_FISCAL_PERIOD"
    VIEW_FISCAL_PERIOD_DETAILS = "VIEW_FISCAL_PERIOD_DETAILS"
    APPROVE_FISCAL_PERIOD_CREATION_OR_MODIFICATION_REQUESTS="APPROVE_FISCAL_PERIOD_CREATION_OR_MODIFICATION_REQUESTS"
    VIEW_ALL_FISCAL_PERIOD_REQUESTS = "VIEW_ALL_FISCAL_PERIOD_REQUESTS"
    AUTHORIZE_FISCAL_PERIOD_CREATION_OR_MODIFICATION_REQUESTS = "AUTHORIZE_FISCAL_PERIOD_CREATION_OR_MODIFICATION_REQUESTS"
    CONFIGURE_GL_CODE = "CONFIGURE_GL_CODE"
    VIEW_ALL_FISCAL_PERIOD_RECORDS = "VIEW_ALL_FISCAL_PERIOD_RECORDS"
    SET_UP_FISCAL_PERIOD = "SET_UP_FISCAL_PERIOD"

    # Currency permissions
    APPROVE_CURRENCY_REQUEST = "APPROVE_CURRENCY_REQUEST"
    CREATE_CURRENCY = "CREATE_CURRENCY"
    DISABLE_CURRENCY = "DISABLE_CURRENCY"
    ENABLE_CURRENCY = "ENABLE_CURRENCY"
    LIST_CURRENCY = "LIST_CURRENCY"
    MODIFY_CURRENCY = "MODIFY_CURRENCY"
    VIEW_CURRENCY_DETAILS = "VIEW_CURRENCY_DETAILS"
    APPROVE_CURRENCY_CREATION_OR_MODIFICATION_REQUESTS = "APPROVE_CURRENCY_CREATION_OR_MODIFICATION_REQUESTS"
    VIEW_ALL_CURRENCY_CONFIGURATION_REQUESTS = "VIEW_ALL_CURRENCY_CONFIGURATION_REQUESTS"
    VIEW_ALL_CURRENCY_RECORDS = "VIEW_ALL_CURRENCY_RECORDS"
    CREATE_NEW_CURRENCY = "CREATE_NEW_CURRENCY"
    RE_OR_DE_ACTIVATE_CURRENCY = "RE_OR_DE_ACTIVATE_CURRENCY"

    # Ledger Permissions
    APPROVE_LEDGER_REQUEST = "APPROVE_LEDGER_REQUEST"
    CREATE_LEDGER = "CREATE_LEDGER"
    DISABLE_LEDGER = "DISABLE_LEDGER"
    ENABLE_LEDGER = "ENABLE_LEDGER"
    LIST_LEDGER = "LIST_LEDGER"
    MODIFY_LEDGER = "MODIFY_LEDGER"
    VIEW_LEDGER_DETAILS = "VIEW_LEDGER_DETAILS"

    # Journal Posting Permissions
    APPROVE_JOURNAL_POSTING_REQUEST = "APPROVE_JOURNAL_POSTING_REQUEST"
    CREATE_JOURNAL_POSTING = "CREATE_JOURNAL_POSTING"
    DISABLE_JOURNAL_POSTING = "DISABLE_JOURNAL_POSTING"
    ENABLE_JOURNAL_POSTING = "ENABLE_JOURNAL_POSTING"
    LIST_JOURNAL_POSTING = "LIST_JOURNAL_POSTING"
    MODIFY_JOURNAL_POSTING = "MODIFY_JOURNAL_POSTING"
    VIEW_JOURNAL_POSTING_DETAILS = "VIEW_JOURNAL_POSTING_DETAILS"
    INITIATE_JOURNAL_POSTING_TRANSACTION = "INITIATE_JOURNAL_POSTING_TRANSACTION"

    #Chart of Account Permissions
    APPROVE_CHART_OF_ACCOUNT_REQUEST = "APPROVE_CHART_OF_ACCOUNT_REQUEST"
    CREATE_CHART_OF_ACCOUNT = "CREATE_CHART_OF_ACCOUNT"
    DISABLE_CHART_OF_ACCOUNT = "DISABLE_CHART_OF_ACCOUNT"
    ENABLE_CHART_OF_ACCOUNT = "ENABLE_CHART_OF_ACCOUNT"
    LIST_CHART_OF_ACCOUNT = "LIST_CHART_OF_ACCOUNT"
    MODIFY_CHART_OF_ACCOUNT = "MODIFY_CHART_OF_ACCOUNT"
    VIEW_CHART_OF_ACCOUNT_DETAILS = "VIEW_CHART_OF_ACCOUNT_DETAILS"

    #FORM BUILDER PERMISSIONS

    CREATE_INDIVIDUAL_CUSTOMER_ACCELERATED_FORMS = "CREATE_INDIVIDUAL_CUSTOMER_ACCELERATED_FORMS"
    CREATE_INDIVIDUAL_CUSTOMER_LEGACY_FORMS = "CREATE_INDIVIDUAL_CUSTOMER_LEGACY_FORMS"
    CREATE_SME_CUSTOMER_ACCELERATED_FORMS = "CREATE_SME_CUSTOMER_ACCELERATED_FORMS"
    CREATE_SME_CUSTOMER_LEGACY_FORMS = "CREATE_SME_CUSTOMER_LEGACY_FORMS"
    MODIFY_INDIVIDUAL_CUSTOMER_ACCELERATED_FORMS = "MODIFY_INDIVIDUAL_CUSTOMER_ACCELERATED_FORMS"
    MODIFY_INDIVIDUAL_CUSTOMER_LEGACY_FORMS = "MODIFY_INDIVIDUAL_CUSTOMER_LEGACY_FORMS"
    MODIFY_SME_CUSTOMER_ACCELERATED_FORMS = "MODIFY_SME_CUSTOMER_ACCELERATED_FORMS"
    MODIFY_SME_CUSTOMER_LEGACY_FORMS  = "MODIFY_SME_CUSTOMER_LEGACY_FORMS"
    VIEW_INDIVIDUAL_CUSTOMER_ACCELERATED_FORMS = "VIEW_INDIVIDUAL_CUSTOMER_ACCELERATED_FORMS"
    VIEW_INDIVIDUAL_CUSTOMER_LEGACY_FORMS = "VIEW_INDIVIDUAL_CUSTOMER_LEGACY_FORMS"
    VIEW_SME_CUSTOMER_ACCELERATED_FORMS = "VIEW_SME_CUSTOMER_ACCELERATED_FORMS"
    VIEW_SME_CUSTOMER_LEGACY_FORMS = "VIEW_SME_CUSTOMER_LEGACY_FORMS"

    #CUSTOMER MANAGEMENT PERMISSIONS
    ACTIVATE_SME_CUSTOMER_SELF_INITIATED = "ACTIVATE_SME_CUSTOMER_SELF_INITIATED"
    ACTIVATE_SME_CUSTOMER_TEAM_INITIATED = "ACTIVATE_SME_CUSTOMER_TEAM_INITIATED"
    CREATE_NEW_INDIVIDUAL_CUSTOMER_ACCELERATED_BULK_CREATION_MODE  = "CREATE_NEW_INDIVIDUAL_CUSTOMER_ACCELERATED_BULK_CREATION_MODE"
    CREATE_NEW_INDIVIDUAL_CUSTOMER_ACCELERATED_SINGLE_CREATION_MODE = "CREATE_NEW_INDIVIDUAL_CUSTOMER_ACCELERATED_SINGLE_CREATION_MODE"
    CREATE_NEW_INDIVIDUAL_CUSTOMER_LEGACY = "CREATE_NEW_INDIVIDUAL_CUSTOMER_LEGACY"
    CREATE_NEW_SME_CUSTOMER_ACCELERATED_BULK_CREATION_MODE = "CREATE_NEW_SME_CUSTOMER_ACCELERATED_BULK_CREATION_MODE"
    CREATE_NEW_SME_CUSTOMER_ACCELERATED_SINGLE_CREATION_MODE = "CREATE_NEW_SME_CUSTOMER_ACCELERATED_SINGLE_CREATION_MODE"
    CREATE_NEW_SME_CUSTOMER_LEGACY = "CREATE_NEW_SME_CUSTOMER_LEGACY"
    DEACTIVATE_INDIVIDUAL_CUSTOMER_SELF_INITIATED = "DEACTIVATE_INDIVIDUAL_CUSTOMER_SELF_INITIATED"
    DEACTIVATE_INDIVIDUAL_CUSTOMER_SYSTEM_WIDE = "DEACTIVATE_INDIVIDUAL_CUSTOMER_SYSTEM_WIDE"
    DEACTIVATE_INDIVIDUAL_CUSTOMER_TEAM_INITIATED = "DEACTIVATE_INDIVIDUAL_CUSTOMER_TEAM_INITIATED"
    DEACTIVATE_SME_CUSTOMER_SELF_INITIATED = "DEACTIVATE_SME_CUSTOMER_SELF_INITIATED"
    DEACTIVATE_SME_CUSTOMER_SYSTEM_WIDE = "DEACTIVATE_SME_CUSTOMER_SYSTEM_WIDE"
    DEACTIVATE_SME_CUSTOMER_TEAM_INITIATED = "DEACTIVATE_SME_CUSTOMER_TEAM_INITIATED"
    MODIFY_INDIVIDUAL_CUSTOMER_PROFILE_SELF_INITIATED = "MODIFY_INDIVIDUAL_CUSTOMER_PROFILE_SELF_INITIATED"
    MODIFY_INDIVIDUAL_CUSTOMER_PROFILE_SYSTEM_WIDE = "MODIFY_INDIVIDUAL_CUSTOMER_PROFILE_SYSTEM_WIDE"
    MODIFY_INDIVIDUAL_CUSTOMER_PROFILE_TEAM_INITIATED = "MODIFY_INDIVIDUAL_CUSTOMER_PROFILE_TEAM_INITIATED"
    MODIFY_SME_CUSTOMER_PROFILE_SELF_INITIATED = "MODIFY_SME_CUSTOMER_PROFILE_SELF_INITIATED"
    MODIFY_SME_CUSTOMER_PROFILE_SYSTEM_WIDE = "MODIFY_SME_CUSTOMER_PROFILE_SYSTEM_WIDE"
    MODIFY_SME_CUSTOMER_PROFILE_TEAM_INITIATED = "MODIFY_SME_CUSTOMER_PROFILE_TEAM_INITIATED"
    REGULARIZE_INDIVIDUAL_CUSTOMER_DOCUMENTS_SELF = "REGULARIZE_INDIVIDUAL_CUSTOMER_DOCUMENTS_SELF"
    REGULARIZE_INDIVIDUAL_CUSTOMER_DOCUMENTS_SYSTEM_WIDE = "REGULARIZE_INDIVIDUAL_CUSTOMER_DOCUMENTS_SYSTEM_WIDE"
    REGULARIZE_INDIVIDUAL_CUSTOMER_DOCUMENTS_TEAM_WIDE = "REGULARIZE_INDIVIDUAL_CUSTOMER_DOCUMENTS_TEAM_WIDE"
    REGULARIZE_SME_CUSTOMER_DOCUMENTS_SELF = "REGULARIZE_SME_CUSTOMER_DOCUMENTS_SELF"
    REGULARIZE_SME_CUSTOMER_DOCUMENTS_SYSTEM_WIDE = "REGULARIZE_SME_CUSTOMER_DOCUMENTS_SYSTEM_WIDE"
    REGULARIZE_SME_CUSTOMER_DOCUMENTS_TEAM_WIDE = "REGULARIZE_SME_CUSTOMER_DOCUMENTS_TEAM_WIDE"
    REQUEST_FOR_DOCUMENT_WAIVER_INDIVIDUAL_CUSTOMERS = "REQUEST_FOR_DOCUMENT_WAIVER_INDIVIDUAL_CUSTOMERS"
    REQUEST_FOR_DOCUMENT_WAIVER_SME_CUSTOMERS = "REQUEST_FOR_DOCUMENT_WAIVER_SME_CUSTOMERS"
    REQUEST_FOR_EDD_CHECK_WAIVER_INDIVIDUAL = "REQUEST_FOR_EDD_CHECK_WAIVER_INDIVIDUAL"
    REQUEST_FOR_EDD_CHECK_WAIVER_SME = "REQUEST_FOR_EDD_CHECK_WAIVER_SME"
    REVIEW_ACTION_BULK_SME_CUSTOMER_CREATION = "REVIEW_ACTION_BULK_SME_CUSTOMER_CREATION"
    REVIEW_ACTION_INDIVIDUAL_CUSTOMER_ACTIVATION_REQUEST = "REVIEW_ACTION_INDIVIDUAL_CUSTOMER_ACTIVATION_REQUEST"
    REVIEW_ACTION_INDIVIDUAL_CUSTOMER_CREATION_REQUEST = "EVIEW_ACTION_INDIVIDUAL_CUSTOMER_CREATION_REQUEST"
    REVIEW_ACTION_INDIVIDUAL_CUSTOMER_DEACTIVATON_REQUEST = "REVIEW_ACTION_INDIVIDUAL_CUSTOMER_DEACTIVATON_REQUEST"
    REVIEW_ACTION_INDIVIDUAL_CUSTOMER_MODIFICATION_REQUEST = "REVIEW_ACTION_INDIVIDUAL_CUSTOMER_MODIFICATION_REQUEST"
    REVIEW_ACTION_INDIVIDUAL_CUSTOMER_PRODUCT_ASSIGNMENT_REQUEST = "REVIEW_ACTION_INDIVIDUAL_CUSTOMER_PRODUCT_ASSIGNMENT_REQUEST"
    REVIEW_ACTION_REGULARIZATION_OF_INDIVIDUAL_CUSTOMER_DOCUMENTS = "REVIEW_ACTION_REGULARIZATION_OF_INDIVIDUAL_CUSTOMER_DOCUMENTS"
    REVIEW_ACTION_REGULARIZATION_OF_SME_CUSTOMER_DOCUMENTS = "REVIEW_ACTION_REGULARIZATION_OF_SME_CUSTOMER_DOCUMENTS"
    REVIEW_ACTION_REQUEST_FOR_DOCUMENT_WAIVER = "REVIEW_ACTION_REQUEST_FOR_DOCUMENT_WAIVER"
    REVIEW_ACTION_REQUEST_FOR_EDD_WAIVER = "EVIEW_ACTION_REQUEST_FOR_EDD_WAIVER "
    REVIEW_ACTION_SME_CUSTOMER_ACTIVATION_REQUEST = "REVIEW_ACTION_SME_CUSTOMER_ACTIVATION_REQUEST"
    REVIEW_ACTION_SME_CUSTOMER_CREATION_REQUEST = "REVIEW_ACTION_SME_CUSTOMER_CREATION_REQUEST"
    REVIEW_ACTION_SME_CUSTOMER_DEACTIVATON_REQUEST = "REVIEW_ACTION_SME_CUSTOMER_DEACTIVATON_REQUEST"
    REVIEW_ACTION_SME_CUSTOMER_MODIFICATION_REQUEST = "REVIEW_ACTION_SME_CUSTOMER_MODIFICATION_REQUEST"
    REVIEW_ACTION_SME_CUSTOMER_MODIFICATION_REQUEST = "REVIEW_ACTION_SME_CUSTOMER_MODIFICATION_REQUEST"
    VIEW_SME_CUSTOMER_DETAILS_CARD = "VIEW_SME_CUSTOMER_DETAILS_CARD"
    VIEW_ALL_INDIVIDUAL_CUSTOMER_RECORDS_SELF = "VIEW_ALL_INDIVIDUAL_CUSTOMER_RECORDS_SELF"
    VIEW_ALL_INDIVIDUAL_CUSTOMER_RECORDS_SELF = "VIEW_ALL_INDIVIDUAL_CUSTOMER_RECORDS_SELF"
    VIEW_ALL_INDIVIDUAL_CUSTOMER_RECORDS_SYSTEM_WIDE = "VIEW_ALL_INDIVIDUAL_CUSTOMER_RECORDS_SYSTEM_WIDE"
    VIEW_ALL_INDIVIDUAL_CUSTOMER_RECORDS_TEAM = "VIEW_ALL_INDIVIDUAL_CUSTOMER_RECORDS_TEAM"
    VIEW_ALL_INDIVIDUAL_CUSTOMER_REQUESTS_SELF = "VIEW_ALL_INDIVIDUAL_CUSTOMER_REQUESTS_SELF"
    VIEW_ALL_INDIVIDUAL_CUSTOMER_REQUESTS_SYSTEM_WIDE = "VIEW_ALL_INDIVIDUAL_CUSTOMER_REQUESTS_SYSTEM_WIDE"
    VIEW_ALL_INDIVIDUAL_CUSTOMER_REQUESTS_TEAM = "VIEW_ALL_INDIVIDUAL_CUSTOMER_REQUESTS_TEAM"
    VIEW_ALL_SME_CUSTOMER_RECORDS_SELF = "VIEW_ALL_SME_CUSTOMER_RECORDS_SELF"
    VIEW_ALL_SME_CUSTOMER_RECORDS_SYSTEM_WIDE = "VIEW_ALL_SME_CUSTOMER_RECORDS_SYSTEM_WIDE"
    VIEW_ALL_SME_CUSTOMER_RECORDS_TEAM = "VIEW_ALL_SME_CUSTOMER_RECORDS_TEAM"
    VIEW_ALL_SME_CUSTOMER_REQUESTS_SELF = "VIEW_ALL_SME_CUSTOMER_REQUESTS_SELF"
    VIEW_ALL_SME_CUSTOMER_REQUESTS_SELF = "VIEW_ALL_SME_CUSTOMER_REQUESTS_SELF"
    VIEW_ALL_SME_CUSTOMER_REQUESTS_SYSTEM_WIDE = "VIEW_ALL_SME_CUSTOMER_REQUESTS_SYSTEM_WIDE"
    VIEW_ALL_SME_CUSTOMER_REQUESTS_TEAM = "VIEW_ALL_SME_CUSTOMER_REQUESTS_TEAM"
    VIEW_ALL_SME_CUSTOMER_REQUESTS_TEAM = "VIEW_ALL_SME_CUSTOMER_REQUESTS_TEAM"
    VIEW_ALL_SME_REQUESTS_SYSTEM_WIDE = "VIEW_ALL_SME_REQUESTS_SYSTEM_WIDE"
    VIEW_INDIVIDUAL_CUSTOMER_DETAILS_CARD = "VIEW_INDIVIDUAL_CUSTOMER_DETAILS_CARD"
    VIEW_PROCESS_SUMMARY_OF_ACTIONED_REQUEST_INDIVIDUAL = "VIEW_PROCESS_SUMMARY_OF_ACTIONED_REQUEST_INDIVIDUAL"
    VIEW_PROCESS_SUMMARY_OF_ACTIONED_REQUEST_SME = "VIEW_PROCESS_SUMMARY_OF_ACTIONED_REQUEST_SME"
    VIEW_SENT_REQUESTS_SYSTEM_WIDE = "VIEW_SENT_REQUESTS_SYSTEM_WIDE"
    VIEW_SENT_REQUESTS_TEAM = "VIEW_SENT_REQUESTS_TEAM"



    # Customer Managment
    VIEW_ALL_INDIVIDUAL_CUSTOMER_RECORDS="VIEW_ALL_INDIVIDUAL_CUSTOMER_RECORDS"
    VIEW_ALL_INDIVIDUAL_CUSTOMER_REQUESTS="VIEW_ALL_INDIVIDUAL_CUSTOMER_REQUESTS"
    VIEW_ALL_CORPORATE_CUSTOMER_RECORDS="VIEW_ALL_CORPORATE_CUSTOMER_RECORDS"
    VIEW_ALL_CORPORATE_CUSTOMER_REQUESTS="VIEW_ALL_CORPORATE_CUSTOMER_REQUESTS"
    CREATE_INDIVIDUAL_CUSTOMER="CREATE_INDIVIDUAL_CUSTOMER"
    CREATE_CORPORATE_CUSTOMER="CREATE_CORPORATE_CUSTOMER"
    RE_OR_DE_ACTIVATE_INDIVIDUAL_CUSTOMER="RE_OR_DE-ACTIVATE_INDIVIDUAL_CUSTOMER"
    RE_DE_ACTIVATE_CORPORATE_CUSTOMER="RE_OR_DE-ACTIVATE_CORPORATE_CUSTOMER"
    CONFIGURE_INDIVIDUAL_CUSTOMER_MANAGEMENT_FORM="CONFIGURE_INDIVIDUAL_CUSTOMER_MANAGEMENT_FORM"
    CONFIGURE_CORPORATE_CUSTOMER_MANAGEMENT_FORM="CONFIGURE_CORPORATE_CUSTOMER_MANAGEMENT_FORM"
    SETUP_INTERIM_APPROVAL_CONFIGURATION_FOR_INDIVIDUAL_CUSTOMERS="SETUP_INTERIM_APPROVAL_CONFIGURATION_FOR_INDIVIDUAL_CUSTOMERS"
    SETUP_INTERIM_APPROVAL_CONFIGURATION_FOR_CORPORATE_CUSTOMERS="SETUP_INTERIM_APPROVAL_CONFIGURATION_FOR_CORPORATE_CUSTOMERS"
    AUTHORIZE_INDIVIDUAL_CUSTOMER_CREATION_MODIFICATION_REQUESTS="AUTHORIZE_INDIVIDUAL_CUSTOMER_CREATION/MODIFICATION_REQUESTS"
    AUTHORIZE_CORPORATE_CUSTOMER_CREATION_MODIFICATION_REQUESTS="AUTHORIZE_CORPORATE_CUSTOMER_CREATION_MODIFICATION_REQUESTS"
    AUTHORIZE_INDIVIDUAL_CUSTOMER_ACTIVATION_DEACTIVATION_REQUESTS="AUTHORIZE_INDIVIDUAL_CUSTOMER_ACTIVATION_DEACTIVATION_REQUESTS"
    AUTHORIZE_CORPORATE_CUSTOMER_ACTIVATION_DEACTIVATION_REQUESTS="AUTHORIZE_CORPORATE_CUSTOMER_ACTIVATION_DEACTIVATION_REQUESTS"
    AUTHORIZE_INDIVIDUAL_CUSTOMER_WAIVER_REQUESTS="AUTHORIZE_INDIVIDUAL_CUSTOMER_WAIVER_REQUESTS"
    AUTHORIZE_CORPORATE_CUSTOMER_WAIVER_REQUESTS="AUTHORIZE_CORPORATE_CUSTOMER_WAIVER_REQUESTS"
    AUTHORIZE_INTERIM_APPROVAL_CONFIGURATION_FOR_INDIVIDUAL_CUSTOMER_REQUESTS="AUTHORIZE_INTERIM_APPROVAL_CONFIGURATION_FOR_INDIVIDUAL_CUSTOMER_REQUESTS"
    AUTHORIZE_INTERIM_APPROVAL_CONFIGURATION_FOR_CORPORATE_CUSTOMER_REQUESTS="AUTHORIZE_INTERIM_APPROVAL_CONFIGURATION_FOR_CORPORATE_CUSTOMER_REQUESTS"
    AUTHORIZE_INDIVIDUAL_CUSTOMER_FORM_SETUP_REQUESTS="AUTHORIZE_INDIVIDUAL_CUSTOMER_FORM_SETUP_REQUESTS"
    AUTHORIZE_CORPORATE_CUSTOMER_FORM_SETUP_REQUESTS="AUTHORIZE_CORPORATE_CUSTOMER_FORM_SETUP_REQUESTS"

    #Product Factory
    VIEW_ALL_DEPOSIT_PRODUCT_RECORDS="VIEW_ALL_DEPOSIT_PRODUCT_RECORDS"
    VIEW_ALL_CREDIT_PRODUCT_RECORDS="VIEW_ALL_CREDIT_PRODUCT_RECORD"
    VIEW_ALL_PAYMENT_PRODUCT_RECORDS="VIEW_ALL_PAYMENT_PRODUCT_RECORDS"
    VIEW_ALL_INVESTMENT_PRODUCT_RECORDS="VIEW_ALL_INVESTMENT_PRODUCT_RECORDS"
    VIEW_ALL_DEPOSIT_PRODUCT_REQUESTS="VIEW_ALL_DEPOSIT_PRODUCT_REQUESTS"
    VIEW_ALL_CREDIT_PRODUCT_REQUESTS="VIEW_ALL_CREDIT_PRODUCT_REQUESTS"
    VIEW_ALL_PAYMENT_PRODUCT_REQUESTS="VIEW_ALL_PAYMENT_PRODUCT_REQUESTS"
    VIEW_ALL_INVESTMENT_PRODUCT_REQUESTS="VIEW_ALL_INVESTMENT_PRODUCT_REQUESTS"
    CREATE_DEPOSIT_PRODUCT="CREATE_DEPOSIT_PRODUCT"
    CREATE_CREDIT_PRODUCT="CREATE_CREDIT_PRODUCT"
    CREATE_PAYMENT_PRODUCT="CREATE_PAYMENT_PRODUCT"
    CREATE_INVESTMENT_PRODUCT="CREATE_INVESTMENT_PRODUCT"
    RE_DE_ACTIVATE_DEPOSIT_PRODUCT="RE_DE_ACTIVATE_DEPOSIT_PRODUCT"
    RE_DE_ACTIVATE_CREDIT_PRODUCT="RE_DE_ACTIVATE_CREDIT_PRODUCT"
    RE_DE_ACTIVATE_PAYMENT_PRODUCT="RE_DE_ACTIVATE_PAYMENT_PRODUCT"
    RE_DE_ACTIVATE_INVESTMENT_PRODUCT="RE_DE_ACTIVATE_INVESTMENT_PRODUCT"
    AUTHORIZE_DEPOSIT_PRODUCT_CREATION_MODIFICATION_REQUESTS="AUTHORIZE_DEPOSIT_PRODUCT_CREATION/MODIFICATION_REQUESTS"
    AUTHORIZE_CREDIT_PRODUCT_CREATION_MODIFICATION_REQUESTS="AUTHORIZE_CREDIT_PRODUCT_CREATION_MODIFICATION_REQUESTS"
    AUTHORIZE_PAYMENT_PRODUCT_CREATION_MODIFICATION_REQUESTS="AUTHORIZE_PAYMENT_PRODUCT_CREATION/MODIFICATION_REQUESTS"
    AUTHORIZE_INVESTMENT_PRODUCT_CREATION_MODIFICATION_REQUESTS="AUTHORIZE_INVESTMENT_PRODUCT_CREATION_MODIFICATION_REQUESTS"
    AUTHORIZE_DEPOSIT_PRODUCT_REACTIVATION_DEACTIVATION_REQUESTS="AUTHORIZE_DEPOSIT_PRODUCT_REACTIVATION/DEACTIVATION_REQUESTS"
    AUTHORIZE_CREDIT_PRODUCT_REACTIVATION_DEACTIVATION_REQUESTS="AUTHORIZE_CREDIT_PRODUCT_REACTIVATION_DEACTIVATION_REQUESTS"
    AUTHORIZE_PAYMENT_PRODUCT_REACTIVATION_DEACTIVATION_REQUESTS="AUTHORIZE_PAYMENT_PRODUCT_REACTIVATION_DEACTIVATION_REQUESTS"
    AUTHORIZE_INVESTMENT_PRODUCT_REACTIVATION_DEACTIVATION_REQUESTS="AUTHORIZE_INVESTMENT_PRODUCT_REACTIVATION/DEACTIVATION_REQUESTS"

    #Concession Group Setup
    VIEW_ALL_INDIVIDUAL_CONCESSION_GROUP_RECORDS="VIEW_ALL_INDIVIDUAL_CONCESSION_GROUP_RECORDS"
    VIEW_ALL_INDIVIDUAL_CONCESSION_GROUP_REQUESTS="VIEW_ALL_INDIVIDUAL_CONCESSION_GROUP_REQUESTS"
    VIEW_ALL_CORPORATE_CONCESSION_GROUP_RECORDS="VIEW_ALL_CORPORATE_CONCESSION_GROUP_RECORDS"
    VIEW_ALL_CORPORATE_CONCESSION_GROUP_REQUESTS="VIEW_ALL_CORPORATE_CONCESSION_GROUP_REQUESTS"
    SET_UP_INDIVIDUAL_GROUP="SET_UP_INDIVIDUAL_GROUP"
    SET_UP_CORPORATE_GROUP="SET_UP_CORPORATE_GROUP"
    RE_DE_ACTIVATE_INDIVIDUAL_GROUP="RE_DE_ACTIVATE_INDIVIDUAL_GROUP"
    RE_DE_ACTIVATE_CORPORATE_GROUP="RE_DE_ACTIVATE_CORPORATE_GROUP"
    AUTHORIZE_INDIVIDUAL_GROUP_CREATION_MODIFICATION_REQUESTS="AUTHORIZE_INDIVIDUAL_GROUP_CREATION_MODIFICATION_REQUESTS"
    AUTHORIZE_CONCESSION_GROUP_CREATION_MODIFICATION_REQUESTS="AUTHORIZE_CONCESSION_GROUP_CREATION_MODIFICATION_REQUESTS"
    AUTHORIZE_INDIVIDUAL_GROUP_REACTIVATION_DEACTIVATION_REQUESTS="AUTHORIZE_INDIVIDUAL_GROUP_REACTIVATION_DEACTIVATION_REQUESTS"
    AUTHORIZE_CORPORATE_GROUP_REACTIVATION_DEACTIVATION_REQUESTS="AUTHORIZE_CORPORATE_GROUP_REACTIVATION_DEACTIVATION_REQUESTS"

    #Charges Management
    VIEW_ALL_CHARGE_RECORDS="VIEW_ALL_CHARGE_RECORDS"
    VIEW_ALL_CHARGE_REQUESTS="VIEW_ALL_CHARGE_REQUESTS"
    CREATE_CHARGE="CREATE_CHARGE"
    RE_DE_ACTIVATE_CHARGE="RE_DE_ACTIVATE_CHARGE"
    AUTHORIZE_CHARGE_CREATION_MODIFICATION_REQUESTS="AUTHORIZE_CHARGE_CREATION/MODIFICATION_REQUESTS"
    AUTHORIZE_CHARGE_ACTIVATION_DEACTIVATION_REQUESTS="AUTHORIZE_CHARGE_ACTIVATION_DEACTIVATION_REQUESTS"

    #Tax Management
    VIEW_ALL_TAX_RECORDS="VIEW_ALL_TAX_RECORDS"
    VIEW_ALL_TAX_REQUESTS="VIEW_ALL_TAX_REQUESTS"
    CREATE_TAX="CREATE_TAX"
    REACTIVATE_DEACTIVATE_TAX="REACTIVATE/DEACTIVATE_TAX"
    AUTHORIZE_TAX_CREATION_MODIFICATION_REQUESTS="AUTHORIZE_TAX_CREATION/MODIFICATION_REQUESTS"
    AUTHORIZE_TAX_ACTIVATION_DEACTIVATION_REQUESTS="AUTHORIZE_TAX_ACTIVATION/DEACTIVATION_REQUESTS"

    #Payments
    VIEW_ALL_TRANSFERS_REQUESTS="VIEW_ALL_TRANSFERS_REQUESTS"
    VIEW_ALL_CASH_TRANSACTION_REQUESTS="VIEW_ALL_CASH_TRANSACTION_REQUESTS"
    VIEW_ALL_BILL_PAYMENT_REQUESTS="VIEW_ALL_BILL_PAYMENT_REQUESTS"
    VIEW_ALL_CHEQUE_TRANSACTION_REQUESTS="VIEW_ALL_CHEQUE_TRANSACTION_REQUESTS"
    CREATE_NEW_TRANSFER="CREATE_NEW_TRANSFER"
    CREATE_NEW_BILL_PAYMENT="CREATE_NEW_BILL_PAYMENT"
    CREATE_NEW_CASH_TRANSACTION="CREATE_NEW_CASH_TRANSACTION"
    CREATE_NEW_CHEQUE_PAYMENT="CREATE_NEW_CHEQUE_PAYMENT"
    AUTHORIZE_TRANSFERS_PAYMENT_REQUESTS="AUTHORIZE_TRANSFERS_PAYMENT_REQUESTS"
    AUTHORIZE_BILL_PAYMENT_PAYMENT_REQUESTS="AUTHORIZE_BILL_PAYMENT_PAYMENT_REQUESTS"
    AUTHORIZE_CASH_TRANSACTION_PAYMENT_REQUESTS="AUTHORIZE_CASH_TRANSACTION_PAYMENT_REQUESTS"
    AUTHORIZE_CHEQUE_PAYMENT_REQUESTS="AUTHORIZE_CHEQUE_PAYMENT_REQUESTS"

    #Team Management
    VIEW_ALL_TEAM_RECORDS="VIEW_ALL_TEAM_RECORDS"
    VIEW_ALL_TEAM_REQUESTS="VIEW_ALL_TEAM_REQUESTS"
    CREATE_SINGLE_TEAM="CREATE_SINGLE_TEAM"
    CREATE_BULK_TEAM="CREATE_BULK_TEAM"
    RE_DE_ACTIVATE_TEAM="RE_DE_ACTIVATE_TEAM"
    AUTHORIZE_CREATION_OR_MODIFICATION_REQUESTS="AUTHORIZE_CREATION_OR_MODIFICATION_REQUESTS"
    AUTHORIZE_REACTIVATION_OR_DEACTIVATION_REQUESTS="AUTHORIZE_REACTIVATION_OR_DEACTIVATION_REQUESTS"
