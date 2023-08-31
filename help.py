def is_int(arg: str) -> bool:
    try:
        int(arg)
        return True
    except ValueError:
        return False


def is_float(arg: str) -> bool:
    try:
        float(arg)
        return True
    except ValueError:
        return False
