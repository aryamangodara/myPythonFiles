n = input()


def check_alpha(n):
    if n in ("abcdefghijklmnopqrstuvwxyz" or "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        return True

    return False


print(check_alpha(n))
