class LoggingDict(dict):
    def __setitem__(self, key, value):
        print(f"Setting {key}: {value}")
        super().__setitem__(key, value)

    def __getitem__(self, value):
        print(f"Getting {value}")
        super().__getitem__(value)

    def __delitem__(self, key):
        print(f"Deleting {key}")
        super().__delitem__(key)


def logging_dict_example():
    print("Logging dict example")
    d = LoggingDict()
    d[0] = "subscribe"
    x = d[0]
    del d[0]
    print()


if __name__ == "__main__":
    logging_dict_example()
