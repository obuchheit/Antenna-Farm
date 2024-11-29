def moxon(freq):
    wave = 299.79/freq

    a = 0.36095 * wave
    b = 0.0575 * wave
    c = 0.0675 * wave

    print(a, b, c)

moxon(146)