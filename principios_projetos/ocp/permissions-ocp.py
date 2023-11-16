class PermissionFactory:
    permission_classes = {
        'admin': AdminPermission,
        'regular': RegularUserPermission,
        # Other permissions can be added here without modifying existing ones
    }

    @classmethod
    def get_permissions(cls, user_type):
        permission_class = cls.permission_classes.get(user_type)
        if permission_class:
            return [permission_class()]
        return [DefaultPermission()]