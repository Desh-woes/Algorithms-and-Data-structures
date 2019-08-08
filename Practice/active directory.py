class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    # First check if user is in current group
    if user in group.get_users():
        return True

    if len(group.get_groups()) == 0:
        return False

    else:
        # Go through the other groups in the current group
        for new_group in group.groups:
            return is_user_in_group(user, new_group)


# Add test cases
# test case 1 - fairly large amount of people in the group

level_11 = Group('a1')

level_21 = Group('b1')
level_22 = Group('b2')
level_23 = Group('b3')

level_11.add_group(level_22)
level_21.add_group(level_22)
level_22.add_group(level_23)
level_23.add_user("timi")



# add_sub_group_users(level_11)
# print(level_11.all_users)

print(is_user_in_group('timi', level_11))  # returns False
