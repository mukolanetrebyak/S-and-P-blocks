def s_block_direct(input_block):
    s_box = [
        [4, 10, 43, 2, 6, 12, 78, 17], #заданий нами S блок
        [1, 2, 11, 0, 15, 31, 14, 19],
        [0, 2, 39, 3, 9, 26, 25, 65, 7],
        [19, 5, 91, 51, 71, 55, 22, 81]
    ]
    tetrad1 = input_block >> 4  #Перша тетрада з 4 першими бітами
    tetrad2 = input_block & 0x0F  #Друга тетрада з 4 іншими бітами
    
    output_tetrad1 = s_block[tetrad1 >> 2][tetrad1 & 0x03] #функція заміни значень за допомогою блоку
    output_tetrad2 = s_block[tetrad2 >> 2][tetrad2 & 0x03]
    
    output_block = (output_tetrad1 << 4) | output_tetrad2
    return output_block
