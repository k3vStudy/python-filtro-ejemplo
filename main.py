def filtrar_mayores(lista: list, may: int):
	"""Toma una lista y filtra los numeros que sean mayores al indicado

	Args:
			lista (list): La lista a filtrar
			may (int): El número mayor

	Returns:
			list: La lista filtrada
	"""
	return [n for n in lista if n > may]


def main():
	may = 10
	lista = [i for i in range(100)]  # Una lista desde el 0 hasta el 99
	lista_filtrada = filtrar_mayores(lista=lista, may=may)
	print("Lista original: ", lista, "\n\nLista filtrada:", lista_filtrada)


if __name__ == '__main__':
	main()
