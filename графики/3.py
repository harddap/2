import matplotlib.pyplot as plt

products = ['помидоры', 'огурцы', 'тыква', 'свекла', 'редис', 'картошка']
quantities = [100, 65, 12, 47, 89, 256]

plt.bar(products, quantities, color='blue')

plt.xlabel('Товар')
plt.ylabel('Количество')
plt.title('Столбчатая диаграмма')

plt.show()
