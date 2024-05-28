class ACL:
    def __init__(self):
        self.users = {}
        self.groups = {}
        self.permissions = {}

    def add_user(self, user):
        if user not in self.users:
            self.users[user] = []
        else:
            print(f"User {user} already exists.")

    def add_group(self, group):
        if group not in self.groups:
            self.groups[group] = []
        else:
            print(f"Group {group} already exists.")

    def add_user_to_group(self, user, group):
        if user in self.users and group in self.groups:
            self.groups[group].append(user)
        else:
            print("User or group does not exist.")

    def set_permission(self, group, resource, permission):
        if group in self.groups:
            if resource not in self.permissions:
                self.permissions[resource] = {}
            self.permissions[resource][group] = permission
        else:
            print(f"Group {group} does not exist.")

    def check_permission(self, user, resource):
        for group in self.groups:
            if user in self.groups[group]:
                if resource in self.permissions and group in self.permissions[resource]:
                    return self.permissions[resource][group]
        return "Access Denied"

# Example Usage
acl = ACL()
acl.add_user("kairat nurtas")
acl.add_group("admin")
acl.add_user_to_group("kairat nurtas", "admin")
acl.set_permission("admin", "file1.txt", "read-write")

print(acl.check_permission("kairat nurtas", "file1.txt"))  # Output: read-write
