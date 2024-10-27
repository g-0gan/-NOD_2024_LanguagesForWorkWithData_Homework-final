class LRUCache:
    """Класс для реализации кэша с алгоритмом Least Recently Used (LRU)."""

    def __init__(self, capacity: int):
        """Инициализирует кэш с заданной емкостью."""
        self.capacity = capacity
        self._cache = {}  # изменено имя на _cache
        self.order = []

    def set_cache(self, key, value):
        """Добавляет новый элемент в кэш и удаляет самый старый, если превышена емкость."""
        if key in self._cache:
            self.order.remove(key)
        elif len(self.order) >= self.capacity:
            oldest_key = self.order.pop(0)
            del self._cache[oldest_key]
        self._cache[key] = value
        self.order.append(key)

    def get(self, key):
        """Получает значение по ключу и обновляет порядок использования."""
        if key in self._cache:
            self.order.remove(key)
            self.order.append(key)
            return self._cache[key]
        return None

    def print_cache(self):
        """Выводит текущий кэш."""
        print("LRU Cache:")
        for key in self.order:
            print(f"{key} : {self._cache[key]}")


# Пример использования
if __name__ == "__main__":
    cache = LRUCache(3)
    cache.set_cache("key1", "value1")
    cache.set_cache("key2", "value2")
    cache.set_cache("key3", "value3")
    cache.print_cache()  # Вывод кэша
    print(cache.get("key2"))  # Получаем значение по ключу
    cache.set_cache("key4", "value4")  # Добавляем новый элемент
    cache.print_cache()  # Обновленный кэш
