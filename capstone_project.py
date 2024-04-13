class ComplaintManagementSystem:
    def __init__(self):
        self.complaints = {}

    def add_complaint(self, complaint_id, title, description):
        if complaint_id in self.complaints:
            print(f"Complaint with ID {complaint_id} already exists.")
        else:
            self.complaints[complaint_id] = {
                'title': title,
                'description': description,
                'status': 'Pending'
            }
            print(f"Complaint with ID {complaint_id} added successfully.")

    def view_complaint(self, complaint_id):
        complaint = self.complaints.get(complaint_id)
        if complaint:
            print(f"Complaint ID: {complaint_id}")
            print(f"Title: {complaint['title']}")
            print(f"Description: {complaint['description']}")
            print(f"Status: {complaint['status']}")
        else:
            print(f"Complaint with ID {complaint_id} not found.")

    def update_status(self, complaint_id, status):
        complaint = self.complaints.get(complaint_id)
        if complaint:
            complaint['status'] = status
            print(f"Status of complaint with ID {complaint_id} updated successfully.")
        else:
            print(f"Complaint with ID {complaint_id} not found.")

    def delete_complaint(self, complaint_id):
        if complaint_id in self.complaints:
            del self.complaints[complaint_id]
            print(f"Complaint with ID {complaint_id} deleted successfully.")
        else:
            print(f"Complaint with ID {complaint_id} not found.")


# Sample usage of the Complaint Management System
if __name__ == "__main__":
    cms = ComplaintManagementSystem()

    cms.add_complaint(1, "Slow Internet", "Internet speed is very slow.")
    cms.add_complaint(2, "No Water Supply", "No water supply in the building.")
    cms.add_complaint(3, "Electricity Outage", "Frequent power outages in the area.")

    cms.view_complaint(2)

    cms.update_status(1, "Resolved")

    cms.view_complaint(1)

    cms.delete_complaint(3)

    cms.view_complaint(3)
