def build_roles_tree(mapping: dict) -> dict:
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    roles_tree = dict()
    categories_list = list()
    for category_id in mapping["categoryIdsSorted"]:
        category = dict()
        category["id"] = f"category-{category_id}"
        category["text"] = mapping["categories"][category_id]["name"]
        category["items"] = [
            {
                "id": mapping["roles"][role_id]["id"],
                "text": mapping["roles"][role_id]["name"],
            }
            for role_id in mapping["categories"][category_id]["roleIds"]
        ]
        categories_list.append(category)
    roles_tree["categories"] = categories_list
    return roles_tree
