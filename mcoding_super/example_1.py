class Base:
    def f(self, x):
        print("Base.f", self, x)


class Derived(Base):
    def f(self, x):
        print("Derived.f", self, x)
        super().f(x)
        print("Derived.f finished")


def basic_example():
    d = Derived()
    d.f(42)


if __name__ == "__main__":
    basic_example()
