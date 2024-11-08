
abeceda = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encode(plaintext, shift):
    posunuty_text = ""
    for pismeno in plaintext:
        if pismeno != " ":
            index = abeceda.index(pismeno)
            novy_index = index + shift
            posunuty_text += abeceda[novy_index]
        else:
            posunuty_text += pismeno
    print(f"Váš šifrovaný text je {posunuty_text}")

def decode(ciphertext, shift):
    text = ""
    for pismeno in ciphertext:
        if pismeno != " ":
            index = abeceda.index(pismeno)
            novy_index = index - shift
            text += abeceda[novy_index]
        else:
            text += pismeno
    print(f"Vás dešifrovaný text je: {text}")

pokracovat = "ok"
while pokracovat == "ok":
    print("CAESAROVA ŠIFRA")
    start = input("encode nebo decode? (e/d)\n")
    text = input("Napiště svůj text:\n").lower()
    shift = int(input("Napiště o kolik pozic se text posune: \n"))

    if start.lower() == "e":
        encode(text, shift)
        pokracovat = input("Napiště 'ok' pro pokračování! Jinak napiš cokoliv jiného. \n")
        if pokracovat != "ok":
            print("Konec programu.")
    elif start.lower() == "d":
        decode(text, shift)
        pokracovat = input("Napiště 'ok' pro pokračování! Jinak napiš cokoliv jiného. \n")
        if pokracovat != "ok":
            print("Konec programu.")
    else: 
        print("Nesprávná hodnota!")