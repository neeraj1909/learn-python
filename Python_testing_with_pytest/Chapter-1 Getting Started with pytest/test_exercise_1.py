"""Test the Task data type."""

from collections import namedtuple

Task = namedtuple('Task', ['summary', 'master', 'status', 'id'])
Task.__new__.__defaults__ = (None, None, 'in progress', None)


def test_dafaults():
    """using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, 's k', 'complete', None)
    assert t1 == t2

def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'hina')
    assert t.summary == 'buy milk'
    assert t.master == 'heena'
    assert (t.done, t.id) == (False, None)
