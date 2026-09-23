# File: test_ordered_set.py

from typing import cast
from unittest import TestCase, main
from ordered_set import OrderedSet


class TestOrderedSet(TestCase):

    a: OrderedSet[int]
    b: OrderedSet[float]
    c: OrderedSet[str]
    d: OrderedSet[None]

    def setUp(self) -> None:
        self.a = OrderedSet(
            [4, 8, 15, 16, 23, 42])
        self.b = OrderedSet(
            [1.7320508076, 3.1415926536, 1.6180339887,
             3.1622776602, 2.7182818285, 1.4142135624])
        self.c = OrderedSet(
            ['Dwalin', 'Balin', 'Fili', 'Kili', 'Dori',
             'Nori', 'Ori', 'Oin', 'Gloin', 'Bifur',
             'Bofur', 'Bombur', 'Thorin'])
        self.d = OrderedSet()

    def test_repr(self) -> None:
        self.assertEqual(
            'OrderedSet([4, 8, 15, 16, 23, 42])',
            repr(self.a))
        self.assertEqual(
            'OrderedSet([1.7320508076, 3.1415926536, '
            '1.6180339887, 3.1622776602, 2.7182818285, '
            '1.4142135624])',
            repr(self.b))
        self.assertEqual(
            "OrderedSet(['Dwalin', 'Balin', 'Fili', 'Kili', "
            "'Dori', 'Nori', 'Ori', 'Oin', 'Gloin', 'Bifur', "
            "'Bofur', 'Bombur', 'Thorin'])",
            repr(self.c))
        self.assertEqual(
            'OrderedSet()',
            repr(self.d))

    def test_contains(self) -> None:
        self.assertTrue(42 in self.a)
        self.assertFalse(24 in self.a)
        self.assertTrue(24 not in self.a)
        self.assertTrue(3.1415926536 in self.b)
        self.assertFalse(2.64575131106 in self.b)
        self.assertTrue(2.64575131106 not in self.b)
        self.assertTrue('Gloin' in self.c)
        self.assertFalse('Gimli' in self.c)
        self.assertTrue('Gimli' not in self.c)
        self.assertFalse(None in self.d)
        self.assertTrue(None not in self.d)

    def test_len(self) -> None:
        self.assertEqual(6, len(self.a))
        self.assertEqual(6, len(self.b))
        self.assertEqual(13, len(self.c))
        self.assertEqual(0, len(self.d))

    def test_add(self) -> None:
        self.a.add(108)
        self.a.add(42)
        self.assertTrue(108 in self.a)
        self.assertEqual(
            'OrderedSet([4, 8, 15, 16, 23, 42, 108])', repr(self.a))
        self.b.add(2.64575131106)
        self.b.add(1.6180339887)
        self.assertTrue(2.64575131106 in self.b)
        self.assertEqual(
            'OrderedSet([1.7320508076, 3.1415926536, '
            '1.6180339887, 3.1622776602, 2.7182818285, '
            '1.4142135624, 2.64575131106])', repr(self.b))
        self.c.add('Gimli')
        self.c.add('Gloin')
        self.assertTrue('Gimli' in self.c)
        self.assertEqual(
            "OrderedSet(['Dwalin', 'Balin', 'Fili', 'Kili', "
            "'Dori', 'Nori', 'Ori', 'Oin', 'Gloin', 'Bifur', "
            "'Bofur', 'Bombur', 'Thorin', 'Gimli'])", repr(self.c))
        self.d.add(None)
        self.d.add(None)
        self.assertTrue(None in self.d)
        self.assertEqual('OrderedSet([None])', repr(self.d))

    def test_discard(self) -> None:
        self.a.discard(8)
        self.a.discard(20)
        self.assertEqual(
            'OrderedSet([4, 15, 16, 23, 42])', repr(self.a))
        self.b.discard(3.1622776602)
        self.b.discard(3.87298334621)
        self.assertEqual(
            'OrderedSet([1.7320508076, 3.1415926536, '
            '1.6180339887, 2.7182818285, 1.4142135624])', repr(self.b))
        self.c.discard('Gloin')
        self.c.discard('Gimli')
        self.assertEqual(
            "OrderedSet(['Dwalin', 'Balin', 'Fili', 'Kili', "
            "'Dori', 'Nori', 'Ori', 'Oin', 'Bifur', 'Bofur', "
            "'Bombur', 'Thorin'])", repr(self.c))
        self.d.discard(None)
        self.assertEqual('OrderedSet()', repr(self.d))

    def test_remove(self) -> None:
        self.a.remove(8)
        with self.assertRaises(KeyError):
            self.a.remove(20)
        self.assertEqual(
            'OrderedSet([4, 15, 16, 23, 42])', repr(self.a))
        self.b.remove(3.1622776602)
        with self.assertRaises(KeyError):
            self.b.remove(3.87298334621)
        self.assertEqual(
            'OrderedSet([1.7320508076, 3.1415926536, '
            '1.6180339887, 2.7182818285, 1.4142135624])', repr(self.b))
        self.c.remove('Gloin')
        with self.assertRaises(KeyError):
            self.c.remove('Gimli')
        self.assertEqual(
            "OrderedSet(['Dwalin', 'Balin', 'Fili', 'Kili', "
            "'Dori', 'Nori', 'Ori', 'Oin', 'Bifur', 'Bofur', "
            "'Bombur', 'Thorin'])", repr(self.c))
        with self.assertRaises(KeyError):
            self.d.remove(None)
        self.assertEqual('OrderedSet()', repr(self.d))

    def test_iter(self) -> None:
        self.assertEqual((4, 8, 15, 16, 23, 42), tuple(iter(self.a)))
        self.assertEqual((1.7320508076, 3.1415926536, 1.6180339887,
                          3.1622776602, 2.7182818285, 1.4142135624),
                         tuple(iter(self.b)))
        self.assertEqual(('Dwalin', 'Balin', 'Fili', 'Kili',
                          'Dori', 'Nori', 'Ori', 'Oin', 'Gloin',
                          'Bifur', 'Bofur', 'Bombur', 'Thorin'),
                         tuple(iter(self.c)))
        for x, y in zip(self.c, list(self.c)):
            self.assertEqual(x, y)
        self.assertEqual((), tuple(iter(self.d)))

    def test_eq(self) -> None:
        a = OrderedSet([15, 8, 23, 4, 42, 16])
        self.assertTrue(a == self.a)
        self.assertTrue(self.a == a)
        a.discard(4)
        a.discard(15)
        a.discard(23)
        self.assertFalse(a == self.a)
        self.assertFalse(cast(OrderedSet[int], OrderedSet()) == self.a)
        b = OrderedSet([3.1415926536, 1.4142135624,
                        1.7320508076, 1.6180339887,
                        3.1622776602, 2.7182818285])
        self.assertTrue(b == self.b)
        self.assertTrue(self.b == b)
        b.discard(3.1415926536)
        b.discard(1.4142135624)
        self.assertFalse(b == self.b)
        self.assertFalse(cast(OrderedSet[float], OrderedSet()) == self.b)
        c = OrderedSet(['Ori', 'Fili', 'Oin',
                        'Gloin', 'Thorin', 'Bifur',
                        'Nori', 'Balin', 'Bombur',
                        'Kili', 'Dwalin', 'Dori',
                        'Bofur'])
        self.assertTrue(c == self.c)
        self.assertTrue(self.c == c)
        c.discard('Kili')
        c.discard('Fili')
        c.discard('Ori')
        c.discard('Dori')
        self.assertFalse(c == self.c)
        self.assertFalse(cast(OrderedSet[str], OrderedSet()) == self.c)
        d = OrderedSet(self.d)
        self.assertTrue(d == self.d)
        self.assertTrue(self.d == d)

    def test_le(self) -> None:
        a = OrderedSet(self.a)
        self.assertTrue(a <= self.a)
        a.discard(4)
        a.discard(15)
        a.discard(23)
        self.assertTrue(a <= self.a)
        self.assertTrue(cast(OrderedSet[int], OrderedSet()) <= self.a)
        b = OrderedSet(self.b)
        self.assertTrue(b <= self.b)
        b.discard(3.1415926536)
        b.discard(1.4142135624)
        self.assertTrue(b <= self.b)
        self.assertTrue(cast(OrderedSet[float], OrderedSet()) <= self.b)
        c = OrderedSet(self.c)
        self.assertTrue(c <= self.c)
        c.discard('Kili')
        c.discard('Fili')
        c.discard('Ori')
        c.discard('Dori')
        self.assertTrue(c <= self.c)
        self.assertTrue(cast(OrderedSet[str], OrderedSet()) <= self.c)
        d = OrderedSet(self.d)
        self.assertTrue(d <= self.d)

    def test_lt(self) -> None:
        a = OrderedSet(self.a)
        self.assertFalse(a < self.a)
        a.discard(4)
        a.discard(15)
        a.discard(23)
        self.assertTrue(a < self.a)
        self.assertTrue(cast(OrderedSet[int], OrderedSet()) < self.a)
        b = OrderedSet(self.b)
        self.assertFalse(b < self.b)
        b.discard(3.1415926536)
        b.discard(1.4142135624)
        self.assertTrue(b < self.b)
        self.assertTrue(cast(OrderedSet[float], OrderedSet()) < self.b)
        c = OrderedSet(self.c)
        self.assertFalse(c < self.c)
        c.discard('Kili')
        c.discard('Fili')
        c.discard('Ori')
        c.discard('Dori')
        self.assertTrue(c < self.c)
        self.assertTrue(cast(OrderedSet[str], OrderedSet()) < self.c)
        d = OrderedSet(self.d)
        self.assertFalse(d < self.d)

    def test_ge(self) -> None:
        a = OrderedSet(self.a)
        self.assertTrue(a >= self.a)
        a.discard(4)
        a.discard(15)
        a.discard(23)
        self.assertFalse(a >= self.a)
        self.assertFalse(cast(OrderedSet[int], OrderedSet()) >= self.a)
        b = OrderedSet(self.b)
        self.assertTrue(b >= self.b)
        b.discard(3.1415926536)
        b.discard(1.4142135624)
        self.assertFalse(b >= self.b)
        self.assertFalse(cast(OrderedSet[float], OrderedSet()) >= self.b)
        c = OrderedSet(self.c)
        self.assertTrue(c >= self.c)
        c.discard('Kili')
        c.discard('Fili')
        c.discard('Ori')
        c.discard('Dori')
        self.assertFalse(c >= self.c)
        self.assertFalse(cast(OrderedSet[str], OrderedSet()) >= self.c)
        d = OrderedSet(self.d)
        self.assertTrue(d >= self.d)

    def test_gt(self) -> None:
        a = OrderedSet(self.a)
        self.assertFalse(a > self.a)
        a.discard(4)
        a.discard(15)
        a.discard(23)
        self.assertTrue(self.a > a)
        self.assertFalse(a > self.a)
        self.assertFalse(cast(OrderedSet[int], OrderedSet()) > self.a)
        b = OrderedSet(self.b)
        self.assertFalse(b > self.b)
        b.discard(3.1415926536)
        b.discard(1.4142135624)
        self.assertTrue(self.b > b)
        self.assertFalse(b > self.b)
        self.assertFalse(cast(OrderedSet[float], OrderedSet()) > self.b)
        c = OrderedSet(self.c)
        self.assertFalse(c > self.c)
        c.discard('Kili')
        c.discard('Fili')
        c.discard('Ori')
        c.discard('Dori')
        self.assertTrue(self.c > c)
        self.assertFalse(c > self.c)
        self.assertFalse(cast(OrderedSet[str], OrderedSet()) > self.c)
        d = OrderedSet(self.d)
        self.assertFalse(d > self.d)

    def test_isdisjoint(self) -> None:
        a: OrderedSet[int] = OrderedSet([7, 17, 27, 37])
        self.assertTrue(self.a.isdisjoint(a))
        a.add(15)
        a.add(42)
        self.assertFalse(self.a.isdisjoint(a))
        a = OrderedSet()
        self.assertTrue(self.a.isdisjoint(a))
        b: OrderedSet[float] = OrderedSet([3.46410161514, 7.07106781187,
                                           10.0])
        self.assertTrue(self.b.isdisjoint(b))
        b.add(3.1415926536)
        self.assertFalse(self.b.isdisjoint(b))
        b = OrderedSet()
        self.assertTrue(self.b.isdisjoint(b))
        c: OrderedSet[str] = OrderedSet(['Legolas', 'Gimli', 'Bilbo', 'Frodo'])
        self.assertTrue(self.c.isdisjoint(c))
        c.add('Thorin')
        c.add('Dori')
        c.add('Bifur')
        c.add('Fili')
        self.assertFalse(self.c.isdisjoint(c))
        c = OrderedSet()
        self.assertTrue(self.c.isdisjoint(c))
        d: OrderedSet[None] = OrderedSet()
        self.assertTrue(self.d.isdisjoint(d))
        d.add(None)
        self.assertTrue(self.d.isdisjoint(d))

    def test_and(self) -> None:
        a: OrderedSet[int] = OrderedSet([42, 8, 20, 108, 15])
        self.assertEqual(
            'OrderedSet([8, 15, 42])',
            repr(self.a & a))
        a = OrderedSet()
        self.assertEqual('OrderedSet()', repr(self.a & a))
        b: OrderedSet[float] = OrderedSet([3.1415926536, 1.0,
                                           1.6180339887,
                                           4.58257569496, 0.0])
        self.assertEqual(
            'OrderedSet([3.1415926536, 1.6180339887])',
            repr(self.b & b))
        b = OrderedSet()
        self.assertEqual('OrderedSet()', repr(b & self.b))
        c: OrderedSet[str] = OrderedSet(['Dori', 'Gimli', 'Bifur',
                                         'Gloin', 'Legolas', 'Balin',
                                         'Thorin', 'Bilbo'])
        self.assertEqual(
            "OrderedSet(['Balin', 'Dori', 'Gloin', "
            "'Bifur', 'Thorin'])",
            repr(self.c & c))
        c = OrderedSet()
        self.assertEqual('OrderedSet()', repr(self.c & c))
        d: OrderedSet[None] = OrderedSet([None])
        self.assertEqual('OrderedSet()', repr(self.d & d))
        d = OrderedSet()
        self.assertEqual('OrderedSet()', repr(self.d & d))

    def test_or(self) -> None:
        a: OrderedSet[int] = OrderedSet([8, 15, 20, 42, 108])
        self.assertEqual(
            'OrderedSet([4, 8, 15, 16, 23, 42, 20, 108])',
            repr(self.a | a))
        a = OrderedSet()
        self.assertEqual(
            'OrderedSet([4, 8, 15, 16, 23, 42])',
            repr(self.a | a))
        b: OrderedSet[float] = OrderedSet([3.1415926536, 1.0,
                                           1.6180339887,
                                           4.58257569496, 0.0])
        self.assertEqual(
            'OrderedSet([1.7320508076, 3.1415926536, '
            '1.6180339887, 3.1622776602, 2.7182818285, '
            '1.4142135624, 1.0, 4.58257569496, 0.0])',
            repr(self.b | b))
        b = OrderedSet()
        self.assertEqual(
            'OrderedSet([1.7320508076, 3.1415926536, '
            '1.6180339887, 3.1622776602, 2.7182818285, '
            '1.4142135624])',
            repr(self.b | b))
        c: OrderedSet[str] = OrderedSet(['Dori', 'Gimli', 'Bifur',
                                         'Gloin','Legolas', 'Balin',
                                         'Thorin', 'Bilbo'])
        self.assertEqual(
            "OrderedSet(['Dwalin', 'Balin', 'Fili', 'Kili', "
            "'Dori', 'Nori', 'Ori', 'Oin', 'Gloin', 'Bifur', "
            "'Bofur', 'Bombur', 'Thorin', 'Gimli', 'Legolas', "
            "'Bilbo'])",
            repr(self.c | c))
        c = OrderedSet()
        self.assertEqual(
            "OrderedSet(['Dwalin', 'Balin', 'Fili', 'Kili', "
            "'Dori', 'Nori', 'Ori', 'Oin', 'Gloin', 'Bifur', "
            "'Bofur', 'Bombur', 'Thorin'])",
            repr(self.c | c))
        d: OrderedSet[None] = OrderedSet([None])
        self.assertEqual('OrderedSet([None])', repr(self.d | d))
        d = OrderedSet()
        self.assertEqual('OrderedSet()', repr(self.d | d))

    def test_sub(self) -> None:
        a: OrderedSet[int] = OrderedSet([8, 15, 20, 42, 108])
        self.assertEqual(
            'OrderedSet([4, 16, 23])',
            repr(self.a - a))
        a = OrderedSet()
        self.assertEqual(
            'OrderedSet([4, 8, 15, 16, 23, 42])',
            repr(self.a - a))
        b: OrderedSet[float] = OrderedSet([3.1415926536, 1.0,
                                           1.6180339887,
                                           4.58257569496, 0.0])
        self.assertEqual(
            'OrderedSet([1.7320508076, 3.1622776602, '
            '2.7182818285, 1.4142135624])',
            repr(self.b - b))
        b = OrderedSet()
        self.assertEqual(
            'OrderedSet([1.7320508076, 3.1415926536, '
            '1.6180339887, 3.1622776602, 2.7182818285, '
            '1.4142135624])',
            repr(self.b - b))
        c: OrderedSet[str] = OrderedSet(['Dori', 'Gimli', 'Bifur',
                                         'Gloin', 'Legolas', 'Balin',
                                         'Thorin', 'Bilbo'])
        self.assertEqual(
            "OrderedSet(['Dwalin', 'Fili', 'Kili', 'Nori', "
            "'Ori', 'Oin', 'Bofur', 'Bombur'])",
            repr(self.c - c))
        c = OrderedSet()
        self.assertEqual(
            "OrderedSet(['Dwalin', 'Balin', 'Fili', 'Kili', "
            "'Dori', 'Nori', 'Ori', 'Oin', 'Gloin', 'Bifur', "
            "'Bofur', 'Bombur', 'Thorin'])",
            repr(self.c - c))
        d: OrderedSet[None] = OrderedSet([None])
        self.assertEqual('OrderedSet()', repr(self.d - d))
        d = OrderedSet()
        self.assertEqual('OrderedSet()', repr(self.d - d))

    def test_xor(self) -> None:
        a: OrderedSet[int] = OrderedSet([8, 15, 20, 42, 108])
        self.assertEqual(
            'OrderedSet([4, 16, 23, 20, 108])',
            repr(self.a ^ a))
        a = OrderedSet()
        self.assertEqual(
            'OrderedSet([4, 8, 15, 16, 23, 42])',
            repr(self.a ^ a))
        b: OrderedSet[float] = OrderedSet([3.1415926536, 1.0, 1.6180339887,
                        4.58257569496, 0.0])
        self.assertEqual(
            'OrderedSet([1.7320508076, 3.1622776602, '
            '2.7182818285, 1.4142135624, 1.0, '
            '4.58257569496, 0.0])',
            repr(self.b ^ b))
        b = OrderedSet()
        self.assertEqual(
            'OrderedSet([1.7320508076, 3.1415926536, '
            '1.6180339887, 3.1622776602, 2.7182818285, '
            '1.4142135624])',
            repr(self.b ^ b))
        c: OrderedSet[str] = OrderedSet(['Dori', 'Gimli', 'Bifur',
                                         'Gloin', 'Legolas', 'Balin',
                                         'Thorin', 'Bilbo'])
        self.assertEqual(
            "OrderedSet(['Dwalin', 'Fili', 'Kili', 'Nori', "
            "'Ori', 'Oin', 'Bofur', 'Bombur', 'Gimli', "
            "'Legolas', 'Bilbo'])",
            repr(self.c ^ c))
        c = OrderedSet()
        self.assertEqual(
            "OrderedSet(['Dwalin', 'Balin', 'Fili', 'Kili', "
            "'Dori', 'Nori', 'Ori', 'Oin', 'Gloin', 'Bifur', "
            "'Bofur', 'Bombur', 'Thorin'])",
            repr(self.c ^ c))
        d: OrderedSet[None] = OrderedSet([None])
        self.assertEqual('OrderedSet([None])', repr(self.d ^ d))
        d = OrderedSet()
        self.assertEqual('OrderedSet()', repr(self.d ^ d))

    def test_clear(self) -> None:
        self.a.clear()
        self.assertEqual('OrderedSet()', repr(self.a))
        self.a.add(108)
        self.assertEqual('OrderedSet([108])', repr(self.a))
        self.b.clear()
        self.assertEqual('OrderedSet()', repr(self.b))
        self.b.add(5.0)
        self.b.add(10.0)
        self.assertEqual('OrderedSet([5.0, 10.0])',
                         repr(self.b))
        self.c.clear()
        self.assertEqual('OrderedSet()', repr(self.c))
        self.c.add('Legolas')
        self.c.add('Frodo')
        self.assertEqual("OrderedSet(['Legolas', 'Frodo'])",
                         repr(self.c))
        self.d.clear()
        self.assertEqual('OrderedSet()', repr(self.d))
        self.d.add(None)
        self.assertEqual('OrderedSet([None])', repr(self.d))

    def test_pop(self) -> None:
        self.assertEqual(42, self.a.pop())
        self.assertEqual(23, self.a.pop())
        with self.assertRaises(KeyError):
            while True:
                self.a.pop()
        self.assertEqual(1.4142135624, self.b.pop())
        self.assertEqual(2.7182818285, self.b.pop())
        self.assertEqual('Thorin', self.c.pop())
        self.assertEqual('Bombur', self.c.pop())
        with self.assertRaises(KeyError):
            self.assertEqual(None, self.d.pop())


if __name__ == '__main__':
    main()
