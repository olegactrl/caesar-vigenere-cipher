import matplotlib.pylab as plt
LETTERS = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
def frequency_analysis(text):
    text = text.upper()
    letter_frequency = {}
    for letter in LETTERS:
        letter_frequency[letter] = 0
    for letter in text:
        if letter in LETTERS:
            letter_frequency[letter] += 1
    return letter_frequency

def plot_distributions(frequencies):
    print(frequencies)
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()

if __name__ == '__main__':
    plain_text = 'Ще не вмерла України і слава, і воля,\
                Ще нам, браття молодії, усміхнеться доля.\
                Згинуть наші воріженьки, як роса на сонці.\
                Запануєм і ми, браття, у своїй сторонці. \
                Душу й тіло ми положим за нашу свободу,\
                І покажем, що ми, браття, козацького роду'
    freq = frequency_analysis(plain_text)
    plot_distributions(freq)