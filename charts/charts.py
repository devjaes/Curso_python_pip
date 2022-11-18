import matplotlib.pyplot as plt


def generate_pychart():
    labels = ['A', 'B', 'C']
    values = [1, 3, 4]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()
