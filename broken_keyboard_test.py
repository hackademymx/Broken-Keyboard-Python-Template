import brokenKeyboard
import collections

def test_broken_keyboard_one():
    print('Test Happy Birthday')
    assert collections.Counter(brokenKeyboard.findBrokenKeys("happy birthday", "hawwy birthday")) == collections.Counter(['p'])

def test_broken_keyboard_two():
    print('Test starry night')
    assert collections.Counter(brokenKeyboard.findBrokenKeys("starry night", "starrq light")) == collections.Counter(['y', 'n'])

def test_broken_keyboard_three():
    print('Test beethoven')
    assert collections.Counter(brokenKeyboard.findBrokenKeys("beethoven", "affthoif5")) == collections.Counter(['b', 'e', 'v', 'n'])

def test_broken_keyboard_four():
    print('Test mozart')
    assert collections.Counter(brokenKeyboard.findBrokenKeys("mozart", "aiwgvx")) == collections.Counter(['m', 'o', 'z', 'a', 'r', 't'])

def test_broken_keyboard_five():
    print('It should work with numbers')
    assert collections.Counter(brokenKeyboard.findBrokenKeys("5678", "4678")) == collections.Counter(['5'])

def test_broken_keyboard_six():
    print('It should work with characters')
    assert collections.Counter(brokenKeyboard.findBrokenKeys("!!??$$", "$$¡¡¿¿")) == collections.Counter(['!', '?'])
