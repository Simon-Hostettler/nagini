from nagini_contracts.contracts import *


class Super:
    def __init__(self, a: int) -> None:
        Ensures(Acc(self.field)) # type: ignore
        Ensures(Acc(self.field2)) # type: ignore
        Ensures(self.field == a) # type: ignore
        Ensures(self.field2 == 12) # type: ignore
        self.field = a
        self.field2 = 12


class Sub(Super):
    def __init__(self, a: int, b: int) -> None:
        Ensures(Acc(self.field)) # type: ignore
        Ensures(Acc(self.field2)) # type: ignore
        Ensures(self.field == a) # type: ignore
        Ensures(self.field2 == 12) # type: ignore
        Ensures(Acc(self.field3)) # type: ignore
        Ensures(self.field3 == b) # type: ignore
        super().__init__(a)
        self.field3 = b


class Other:
    def __init__(self) -> None:
        Ensures(Acc(self.field2)) # type: ignore
        Ensures(self.field2 == 12) # type: ignore
        self.field2 = 12


class Empty:
    pass


def main() -> None:
    a = Empty()
    Assert(isinstance(a, Empty))

    b = Other()
    Assert(isinstance(b, Other))
    Assert(b.field2 == 12)
    b.field2 = 14
    Assert(b.field2 == 14)

    c = Super(45)
    Assert(isinstance(c, Super))
    Assert(c.field == 45)
    Assert(c.field2 == 12)
    c.field2 = 14
    Assert(c.field2 == 14)

    d = Sub(46, 32)
    Assert(isinstance(d, Super))
    Assert(isinstance(d, Sub))
    Assert(d.field == 46)
    Assert(d.field2 == 12)
    Assert(d.field3 == 32)

    #:: ExpectedOutput(assert.failed:assertion.false)
    Assert(c.field == 14)