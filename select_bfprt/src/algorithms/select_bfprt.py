import math 

from algorithms.merge_sort import merge_sort

def select_bfprt_factory(partition_size):
    def select_bfprt(array, n, k):
        median_of_medians = SelectBFPRT(array, n, partition_size)
        return median_of_medians.find_kth_biggest(k)

    return select_bfprt

class SelectBFPRT:
    def __init__(self, array, n, partition_size=5):
        self.array = array
        self.n = n
        self.partition_size = partition_size

    """
        Como queremos a K-ésima maior posição do array e 
        a função select_bfprt retorna a posição do K-ésimo menor elemento,
        então, para encontrar a posição do K-ésimo maior elemento,
        basta inverter o array e passar o parâmetro i = n - i + 1
    """
    def find_kth_biggest(self, i):
        k = self.n - i + 1
        k_smalest_index = self.select_bfprt(self.array, 0, self.n - 1, k)
        return self.array[k_smalest_index]

    """
        Retorna o K-ésimo menor elemento do array
    """
    def select_bfprt(self, array, p, r, i):
        n = r - p + 1

        if p == r:
            return p

        q = self.partition_bfprt(array, p, r)
        k = q - p + 1

        if i == k:
            return q

        # Se i for menor que k, então o K-ésimo menor elemento está no lado esquerdo do array
        if k > i:
            return self.select_bfprt(array, p, q - 1, i)

        # Se i for maior que k, então o K-ésimo menor elemento está no lado direito do array
        return self.select_bfprt(array, q + 1, r, i - k)


    def partition_bfprt(self, array, p, r):
        # Divide o array em grupos de 5 elementos
        n = r - p + 1
        median_offset = self.partition_size // 2
        groups_quantity = math.ceil(n / self.partition_size)

        # Ordena todos os grupos, exceto o último
        for i in range(groups_quantity - 1):
            start = p + self.partition_size * i
            end = p + self.partition_size * (i + 1) - 1
            merge_sort(array, start, end)

        # Ordena o último grupo
        last_group_size = n % self.partition_size
        last_group_start = p + self.partition_size * (groups_quantity - 1)
        last_group_end = n - 1
        merge_sort(array, last_group_start, last_group_end)

        # Troca a mediana de cada grupo para as primeiras posições do array
        for i in range(groups_quantity - 1):
            index_at_median_group = p + i
            median_index = p + self.partition_size * i + median_offset
            array[index_at_median_group], array[median_index] = array[median_index], array[index_at_median_group]

        last_index_at_median_group = p + groups_quantity - 1
        last_median_index = last_group_start + last_group_size // 2
        array[last_median_index], array[last_index_at_median_group] = array[last_index_at_median_group], array[last_median_index]

        # Verifica qual K-ésimo menor elemento é a mediana das medianas, pois
        # essas medianas estão desordenadas e podem crescer indefinidamente
        start_median_array = p
        end_median_array = p + groups_quantity - 1    
        index_median_of_medians = math.ceil(groups_quantity / 2)

        k_smalest_index = self.select_bfprt(array, start_median_array, end_median_array, index_median_of_medians)
        array[k_smalest_index], array[r] = array[r], array[k_smalest_index]

        return partition(array, p, r)

def partition(array, p, r):
    pivot = array[r]
    i = p - 1

    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[r] = array[r], array[i + 1]

    return i + 1
