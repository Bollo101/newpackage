from newpackage import myModule

def top_n_test():
    '''
    make sure top_n works correctly
    '''
    assert myModule.top_n([9,8,5,2,7]) ==[9,8,7], 'inccorect'
    assert myModule.top_n([9,8,5,2,7,10,19]) ==[19,10,9], 'inccorect'
    assert myModule.top_n([9,8,5,2,7,100,6,86]) ==[100,86,9], 'inccorect'