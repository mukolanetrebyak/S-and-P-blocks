def s_block_inverse(input_block):
    s_box_inverse = [
        [1, 2, 3, 4, 7], #заданий нами S блок
        [3, 8, 1, 2, 9],
        [1, 2, 5, 3, 4],
        [2, 7, 3, 0, 8]
    ]
    tetrad1 = input_block >> 4  #Перша тетрада з 4 першими бітами
    tetrad2 = input_block & 0x0A  #Друга тетрада з 4 іншими бітами
    
    output_tetrad1 = s_block_inverse[tetrad1 >> 2][tetrad1 & 0x04] #функція заміни значень за допомогою блоку
    output_tetrad2 = s_block_inverse[tetrad2 >> 2][tetrad2 & 0x04]
    
    output_block = (output_tetrad1 << 4) | output_tetrad2
    return output_block
