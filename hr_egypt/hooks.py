from . import __version__ as app_version

app_name = "hr_egypt"
app_title = "Hr Egypt"
app_publisher = "Mahmoud"
app_description = "HR Egypt"
app_email = "erpnext@zamiltec.com"
app_license = "MIT"

fixtures = [
    # {"dt": "DocType", "filters": [
    #     [
    #         "name", "in", [
    #             "Responsible area",
    #             "Responsible area table"
    #         ]
    #     ]
    # ]},
    # {"dt": "Custom Field", "filters": [   
    #         ["Fieldname", "in", [
    #             "zt_end_of_health_insurance",
    #             "zt_has_health_insurance",
    #             "zt_employee_age",
    #             "zt_probation_period_date",
    #             "zt_responsible_area",
    #             "zt_employee_salary_payment_id",
    #         ]]
    
    # ]},    
    {"dt": "Custom Field", "filters": [
        [
            "Fieldname", "like", "zt_%" 
        ]     
    ]
    }  
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hr_egypt/css/hr_egypt.css"
# app_include_js = "/assets/hr_egypt/js/hr_egypt.js"

# include js, css files in header of web template
# web_include_css = "/assets/hr_egypt/css/hr_egypt.css"
# web_include_js = "/assets/hr_egypt/js/hr_egypt.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hr_egypt/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "hr_egypt.utils.jinja_methods",
#	"filters": "hr_egypt.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hr_egypt.install.before_install"
# after_install = "hr_egypt.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hr_egypt.uninstall.before_uninstall"
# after_uninstall = "hr_egypt.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hr_egypt.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Employee": {
		"validate": "hr_egypt.hr_egypt.doctype.responsible_area.responsible_area.update_employee_data",
	}
}

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"hr_egypt.tasks.all"
#	],
#	"daily": [
#		"hr_egypt.tasks.daily"
#	],
#	"hourly": [
#		"hr_egypt.tasks.hourly"
#	],
#	"weekly": [
#		"hr_egypt.tasks.weekly"
#	],
#	"monthly": [
#		"hr_egypt.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "hr_egypt.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "hr_egypt.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "hr_egypt.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hr_egypt.utils.before_request"]
# after_request = ["hr_egypt.utils.after_request"]

# Job Events
# ----------
# before_job = ["hr_egypt.utils.before_job"]
# after_job = ["hr_egypt.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"hr_egypt.auth.validate"
# ]
