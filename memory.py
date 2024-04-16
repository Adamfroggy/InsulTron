from typing import List


class ShortTermMemory:
    def __init__(self, name: str, capacity: int = 10):
        self.name = name
        self.capacity = capacity
        self.memory = []

    def insert(self, message: str) -> None:
        if len(self.memory) >= self.capacity:
            self.memory.pop(0)  # Remove the oldest message if capacity reached
        self.memory.append(message)

    def recent(self, n: int = 10) -> List[str]:
        return self.memory[-n:]

    def clear(self) -> None:
        self.memory = []

    def __str__(self) -> str:
        return "\n".join(self.memory)
