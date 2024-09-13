import base64


def LeggiBinario(pin, pout):
    with open(pin, mode="rb") as fin:
        with open(pout, mode="w") as fou:
            dati = fin.read()
            for v in dati:
                fou.write(str(bytes(v),))
                fou.write("\n")


def ScriviBinario(tin, tou):
    with open(tin, mode="r") as fin:
        with open(tou, mode="wb") as fou:
            nums = fin.readlines()
            for num in nums:
                a = int(num).to_bytes()
                fou.write(a)


# esempio
LeggiBinario("pitone.jpeg", "pitone.txt")
ScriviBinario("pitone.txt", "pitone1.jpeg")
