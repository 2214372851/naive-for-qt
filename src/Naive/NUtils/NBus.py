

class NBus(type):
    """
    Used to implement singleton mode, Global event bus
    """
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = cls.__new__(cls)
        cls.__init__(cls.instance, *args, **kwargs)
        return cls.instance
