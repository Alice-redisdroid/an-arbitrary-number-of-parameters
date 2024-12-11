def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        word = word.lower()
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)

    print(same_words)

single_root_words('oksel', 'Tokselvania', 'orcoer', 'Oksel')
single_root_words('Tsuki', 'Uki', 'orcoer', 'SaTsUki')



