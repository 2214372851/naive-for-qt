class NMetaClass(type):
    """
    A metaclass that ensures that only one instance of a class can be created.
    """

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = cls.__new__(cls)
        cls.__init__(cls.instance, *args, **kwargs)
        return cls.instance
