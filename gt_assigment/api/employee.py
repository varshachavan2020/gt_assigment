import frappe


def before_save(doc, method=None):
    """Hook to execute logic before saving an Employee document."""
    if doc.workflow_state == "Exited":
        pdf = frappe.attach_print(
            doctype="Employee",
            name=doc.name,
            print_format="Experience Letter",
            doc=doc
        )
        frappe.sendmail(
            recipients=doc.personal_email,
            subject="Your Experience Letter",
            message="Please find attached your Experience Letter.",
            attachments=[pdf]
        )
