




img = np.array((list('abcd'), list('efgh'), list('ijkl')))
print_img(img)
print("")
print_img(cut_off_edges(img))

img_str = \
"""
###               O 
#    ##    ##    ###
#  #  #  #  #  #    
""".replace(' ', '.')
img = img_from_strings(img_str.split('\n'))
print('img', img)
print_img(img)

print(find_non_dot(img))
