def moxon(freq):
    #https://w4.vp9kf.com/moxon_design.htm
    wave = 299.7925/freq

    a = 0.33985 * wave
    b = 0.05165 * wave
    c = 0.07178 * wave

    print(a, b, c)

moxon(146)