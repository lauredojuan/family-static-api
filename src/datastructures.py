
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
import uuid

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members =[
                        #  { "id": "0000000001","first_name": "John" ,  "age": 33, "Lucky Numbers": [7, 13, 22] },
                        #  { "id": "0000000002","first_name": "Jane" ,  "age": 35, "Lucky Numbers": [10, 14, 3] },
                        #  { "id": "0000000003","first_name": "Jimmy" , "age": 5, "Lucky Numbers": [1] }
                        ] 


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        # return randint(0, 99999999)
        return uuid.uuid4()

    def add_member(self, member):
        self._members.append(member)
        # fill this method and update the return
        return None

        
    def delete_member(self, id):
        # fill this method and update the return

        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
                return None
        

    def get_member(self, id):
        # fill this method and update the return
        for m in self._members:
            if m["id"] == id:
                return m

        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members