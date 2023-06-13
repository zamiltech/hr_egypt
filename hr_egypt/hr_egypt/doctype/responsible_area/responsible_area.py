# Copyright (c) 2023, Mahmoud and contributors
# For license information, please see license.txt
from dateutil.relativedelta import relativedelta

import frappe
from frappe.model.document import Document
from frappe.utils import getdate


class Responsiblearea(Document):
	pass


def update_employee_data(doc, method):
	# called via User hook
	age_str = ""
	employee = doc #frappe.get_doc("Employee", doc.name)
	born = getdate(employee.date_of_birth)
	age = relativedelta(getdate(), born)
	age_str = str(age.years) + " year(s) " + str(age.months) + " month(s) " + str(age.days) + " day(s)"
	employee.zt_employee_age = age_str
	# frappe.msgprint(age_str)
	#employee.update_user_permissions()