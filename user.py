class User:
def init(self, user_id, name, email):
self.user_id = user_id
self.name = name
self.email = email

def display_user(self):
    print("User ID:", self.user_id)
    print("Name:", self.name)
    print("Email:", self.email)