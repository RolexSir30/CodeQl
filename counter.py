from collections import Counter import python

def frequency_sort(nums):
    """
    Trie une liste d'entiers par fréquence d'apparition (en ordre croissant),
    et en cas d'égalité, par ordre croissant des valeurs.
    
    :param nums: Liste d'entiers à trier.
    :return: Liste triée.
    """
    if not isinstance(nums, list):
        raise ValueError("L'entrée doit être une liste.")

    freq_count = Counter(nums)
    return sorted(nums, key=lambda x: (freq_count[x], x))
