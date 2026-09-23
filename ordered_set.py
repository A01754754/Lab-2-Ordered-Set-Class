#----------------------------------------------------------
# Lab #2: Ordered Set Class
# Implementation of a generic ordered set class and its
# corresponding operations.
#
# Date: 23-Sep-2026
# Authors:
#           A01754754 Alexis Maximiliano Alva Martínez
#           A01754717 Nestor Daniel
#----------------------------------------------------------

from typing import cast
from collections.abc import Iterator, Iterable


class OrderedSet[T]:

    class Node[N]:

        info: N
        next: OrderedSet.Node[N]
        prev: OrderedSet.Node[N]

        # Complexity: O(1)
        def __init__(self, value: N) -> None:
            self.info = value
            self.next = self
            self.prev = self

    __sentinel: OrderedSet.Node[T]
    __count: int

    # Complexity: O(N), N = len(values)
    def __init__(self, values: Iterable[T] = ()) -> None:
        self.__sentinel = OrderedSet.Node(cast(T, None))
        self.__count = 0
        for elem in values:
            self.add(elem)

    # Complexity: O(1)
    def __len__(self) -> int:
        return self.__count

    # Complexity: O(N)
    def __repr__(self) -> str:
        return f'OrderedSet({list(self) if self else ""})'

    # Complexity: O(N)
    def add(self, value: T) -> None:
        if value in self:
            return
        self.__count += 1
        new_node: OrderedSet.Node[T] = OrderedSet.Node(value)
        new_node.prev = self.__sentinel.prev
        new_node.next = self.__sentinel
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity: O(N)
    def __iter__(self) -> Iterator[T]:
        current: OrderedSet.Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            yield current.info
            current = current.next

    # Complexity: O(N)
    def __contains__(self, value: object) -> bool:
        for elem in self:
            if elem == value:
                return True
        return False

    # Complexity: O(N)
    def discard(self, value: T) -> None:
        current: OrderedSet.Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            if current.info == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.__count -= 1
                return
            current = current.next

    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        if not isinstance(other, OrderedSet):
            return False
        if len(self) != len(cast(OrderedSet[T], other)):
            return False
        for elem in self:
            if elem not in other:
                return False
        return True

    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __le__(self, other: OrderedSet[T]) -> bool:
        if self is other:
            return True
        if len(self) > len(other):
            return False
        for elem in self:
            if elem not in other:
                return False
        return True

    # Complexity: O(N*M) where N = len(self) and M = len(other)
    def __and__(self, other: OrderedSet[T]) -> OrderedSet[T]:
        result: OrderedSet[T] = OrderedSet()
        for elem in self:
            if elem in other:
                result.add(elem)
        return result


if __name__ == '__main__':
    a: OrderedSet[int] = OrderedSet([4, 8, 15, 16, 23])
    b: OrderedSet[int] = OrderedSet([23, 16, 8, 4, 15])
    print(a == b)
    print(a == 42)
    print(a == a)
    a.discard(23)
    print(a == b)