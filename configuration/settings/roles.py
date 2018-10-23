from rolepermissions.roles import AbstractUserRole


class ApiUser(AbstractUserRole):
    available_permissions = {
        ('can_create_view_via_API', 'Create or View via API'),
        ('can_view_via_API', 'Create View only via API'),
    }


class ShoRole1(AbstractUserRole):
    available_permissions = {
        'permission1': True,
        'permission2': True,
    }


class ShoRole2(AbstractUserRole):
    available_permissions = {
        'permission3': True,
        'permission4': False,
    }


class ShoRole3(AbstractUserRole):
    role_name = 'sho_new_name'
    available_permissions = {
        'permission5': False,
        'permission6': False,
    }


class ShoRole4(AbstractUserRole):
    available_permissions = {
        'permission1': False,
        'permission3': False,
    }


