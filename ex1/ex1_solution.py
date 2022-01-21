def __rename_key_name2text(dict2process: dict) -> dict:
    dict2process["text"] = dict2process.pop("name")
    return dict2process


def __process_role_map(role: dict) -> dict:
    role_processed = dict(role)
    return __rename_key_name2text(role_processed)


def __process_category_map(category: dict, roles: dict) -> dict:
    category_processed = dict(category)
    __rename_key_name2text(category_processed)
    category_processed["id"] = f"category-{category_processed['id']}"
    category_processed["items"] = [
        __process_role_map(roles[role_id]) for role_id in category_processed["roleIds"]
    ]
    category_processed.pop("roleIds")
    return category_processed


def build_roles_tree(mapping: dict) -> dict:
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    roles_tree = dict()

    roles_tree["categories"] = [
        __process_category_map(mapping["categories"][category_id], mapping["roles"])
        for category_id in mapping["categoryIdsSorted"]
    ]
    return roles_tree
