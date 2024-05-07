def bisection_method(f, a, b, tol, max_iter):
    """
    Bisection Method ile kök bulma fonksiyonu.

    :param f: Kökü bulunacak fonksiyon.
    :param a: Aralığın alt sınırı.
    :param b: Aralığın üst sınırı.
    :param tol: Tolerans (hata payı).
    :param max_iter: Maksimum iterasyon sayısı.
    :return: Kök yaklaşımı ve iterasyon sayısı.
    """
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2, iter_count


def bisection_last_root(f, a, b, tol, max_iter):
    """
    Bir aralıktaki son kökü bulan fonksiyon.

    :param f: Kökü bulunacak fonksiyon.
    :param a: Aralığın alt sınırı.
    :param b: Aralığın üst sınırı.
    :param tol: Tolerans (hata payı).
    :param max_iter: Maksimum iterasyon sayısı.
    :return: Son kök ve iterasyon sayısı.
    """
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2, iter_count


# Örnek kullanım:
# Kökü bulunacak fonksiyon: x^3 - 6x^2 + 11x - 6
f = lambda x: x**5 - 7*x**2 + 11*x - 14

# Aralık: [0, 4]
a = 0
b = 4

# Tolerans ve maksimum iterasyon sayısı
tolerans = 0.0001
max_iterasyon = 1000

# Bisection Method'u genelleştirilmiş fonksiyonu uygula
son_kok, iterasyon_sayisi = bisection_last_root(f, a, b, tolerans, max_iterasyon)

print(f"Son bulunan kök: {son_kok}:değer:{f(son_kok)}")
