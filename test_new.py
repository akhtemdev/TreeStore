from typing import Union


class TreeStore:
    """Класс TreeStore."""

    def __init__(self, items: list[dict[str, Union[int, str, None]]]) -> None:
        self.items: list = items

        self.id_to_item: dict = {item['id']: item for item in items}

        self.parent_to_children: dict = {}
        for item in items:
            parent = item['parent']
            if parent not in self.parent_to_children:
                self.parent_to_children[parent] = []
            self.parent_to_children[parent].append(item)

    def getAll(self) -> list[dict[str, Union[int, str, None]]]:
        """Возвращает изначальный массив элементов."""
        return self.items

    def getItem(self, id: int) -> dict[str, Union[int, str, None]] | None:
        """Принимает id элемента и возвращает сам объект элемента."""
        return self.id_to_item.get(id, None)

    def getChildren(self, id: int) -> list[dict[str, Union[int, str, None]]]:
        """Принимает id элемента и возвращает массив элементов,
        являющихся дочерними для того элемента.
        """
        return self.parent_to_children.get(id, [])

    def getAllParents(self, id: int) -> list[dict[str, Union[int, str, None]]]:
        """Принимает id элемента и возвращает массив
        из цепочки родительских элементов.
        """
        parents = []
        current_item = self.getItem(id)

        while current_item and current_item['parent'] != 'root':
            parent_id = current_item['parent']
            parent_item = self.getItem(parent_id)
            if parent_item:
                parents.append(parent_item)
            current_item = parent_item
        return parents
