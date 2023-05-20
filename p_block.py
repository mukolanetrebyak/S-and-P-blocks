def p_block(input_block):
    block_table = [10, 4, 33, 12, 6, 8, 5, 7]   #таблиця перестановок
    output_block = 0                            #вихідний блок даних
    
    for i, bit_index in enumerate(block_table): #функція перестановки біта 
        if (input_block >> (8 - bit_index)) & 0x08:
            output_block |= 1 << (8 - i)
    
    return output_block
