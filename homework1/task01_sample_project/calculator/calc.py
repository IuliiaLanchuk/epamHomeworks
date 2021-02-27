def check_power_of_2(a: int) -> bool:
    return type(a) == int and a != 0 and not (bool(a & (a - 1)))
