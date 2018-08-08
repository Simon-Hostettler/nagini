from nagini_contracts.lock import Lock
from nagini_contracts.contracts import *
from nagini_contracts.obligations import Level, WaitLevel


class Cell:
    def __init__(self, val: int) -> None:
        self.value = val
        Ensures(Acc(self.value) and self.value == val)


class CellLock(Lock[Cell]):

    @Predicate
    def invariant(self) -> bool:
        return Acc(self.get_locked().value) and LowVal(self.get_locked().value)

def client(secret: bool) -> None:
    c = Cell(1)
    l = CellLock(c)
    l.acquire()
    Unfold(l.invariant())
    c.value = 4
    if secret:
        Fold(l.invariant())
        #:: ExpectedOutput(call.precondition:assertion.false)
        l.release()
        l.acquire()
        Unfold(l.invariant())
    c.value = 5
    Fold(l.invariant())
    l.release()

