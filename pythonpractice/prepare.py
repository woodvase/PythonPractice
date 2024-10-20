from collections import OrderedDict
from threading import Lock

lock = Lock()

ord_dict = OrderedDict().fromkeys("GeeksForGeeks")
print("Original Dictionary")
print(ord_dict)

# Move the key to  end
with lock:
    ord_dict.move_to_end("e")
print("\nAfter moving key 'G' to end of dictionary :")
print(ord_dict)

# Move the key to beginning
ord_dict.move_to_end("k", last=False)
print("\nAfter moving Key in the Beginning :")
print(ord_dict)


class Class1:
    def __init__(self):
        self.a = "a"


class _Class1:
    def __init__(self) -> None:
        pass
