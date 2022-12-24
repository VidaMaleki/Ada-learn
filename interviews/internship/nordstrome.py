# 
# Our designers have given us two lists of all the possible BEIGE colors and they would to find which
# colors are in both lists, only found in list 1 and only found in 2.
#
# 1. Write a function that creates lists (or other collection) 
#    for colors common in both, unique in list1 and unique in list2.
# 2. Print the results returned from the function
#
# For example, 
#      list1=[ "RED", "BLUE", "PURPLE"]
#      list2=[ "BLUE", "PINK", "RED"]
#
# The results would be : 
#      Found in both
#          BLUE
#          RED
#      Found in list 1 only
#          PURPLE
#      Found in list 2 only
#          PINK
#    

# Convert the lists to set
# Intersection of both sets
# Difference between set1 and set2
# Difference between set1 and set2

def common_and_unique(arr1,arr2):
  set_1 = set(arr1)
  set_2 = set(arr2)

  common_colors = set_1 & set_2
  unique_1 = set_1 - set_2
  unique_2 = set_2 - set_1

  print("The common colors are", list(common_colors))
  print("The colors that are unique to list1", list(unique_1))
  print("The colors that are unique to list2", list(unique_2))


list1 = [ "BEIGE CEMENT", "BEIGE NOVELLE", "BEIGE LINEN", "BEIGE OVERCAST", "BEIGE MARBLE", "BEIGE WOOD", "BEIGE MELLOW", "BEIGE MOJAVE", "BEIGE PEBBLE", "BEIGE SEASHORE", "BEIGE BIRCH", "BEIGE QUARTZ", "BEIGE TINT", "BEIGE CLAY", "BEIGE ANGORA", "BEIGE CRYSTAL", "BEIGE SMOKE", "BEIGE BEACH", "BEIGE GOAT", "BEIGE SUNBURST", "BEIGE DESERT", "BEIGE SAND", "BEIGE SEMOLINA- PINK PACK", "BEIGE BLONDE", "BEIGE DUST", "BEIGE HAZE", "BEIGE VANILLA", "BEIGE BUFF", "BEIGE FADED", "BEIGE HAZELNUT", "BEIGE OLIVE", "BEIGE TAPIOCA", "BEIGE SHELL", "BEIGE ILLUSION", "BEIGE AMBER", "BEIGE MAPLE", "BEIGE", "BEIGE ALESAN", "BEIGE BURNT", "BEIGE SCROLL", "BEIGE GRAVEL", "BEIGE CURRY", "BEIGE DUNE", "BEIGE MOTH", "BEIGE BISCUIT", "BEIGE HUMUS", "BEIGE MARZIPAN", "BEIGE BLUSH", "BEIGE KISS", "BEIGE DAWN", "BEIGE DEER", "BEIGE PEACH", "BEIGE NUT", "BEIGE OATMEAL", "BEIGE FRAPPE", "BEIGE PUREE", "BEIGE SUMMER", "BEIGE PRUNUS", "BEIGE STRAW" ]


list2 = [ "BEIGE PRUNUS", "BEIGE ANGORA", "BEIGE DAWN", "BEIGE BLISS", "BEIGE WHEAT", "BEIGE GOAT", "BEIGE TENDER", "BEIGE GRAIN", "BEIGE MOONLIGHT", "BEIGE BRUSH", "BEIGE RUGBY", "BEIGE SILVER", "BEIGE BLOSSOM", "BEIGE SHIFTING", "BEIGE NOUGAT", "BEIGE BUFF", "BEIGE SUNBURST", "BEIGE OYSTER", "BEIGE BLUSH", "BEIGE CREAM", "BEIGE SHEEPSKIN", "BEIGE MORN", "BEIGE HAZELNUT", "BEIGE MOSAIC", "BEIGE PEARLED", "BEIGE TUSCANY", "BEIGE TAPIOCA", "BEIGE RAINY DAY", "BEIGE WHISPER", "BEIGE BEAN", "BEIGE BIRCH", "BEIGE PEBBLE", "BEIGE PARSNIP", "BEIGE SAND", "BEIGE OAK", "BEIGE NUT", "BEIGE FAWN", "BEIGE BISQUE", "BEIGE FRAPPE", "BEIGE WINTER", "BEIGE ECRU", "BEIGE MARBLE", "BEIGE SWAN", "BEIGE TINT", "BEIGE SEMOLINA", "BEIGE DUNE", "BEIGE KHAKI", "BEIGE AMBER", "BEIGE DEER", "BEIGE PORCELAIN", "BEIGE VANILLA", "BEIGE PUMICE", "BEIGE APRICOT", "BEIGE BISCUIT", "BEIGE CASTLE", "BEIGE ALMOND", "BEIGE JOY", "BEIGE PARCHMENT", "BEIGE ROSE", "BEIGE CURRY", "BEIGE ALESAN", "BEIGE SEASHORE", "BEIGE OLIVE", "BEIGE PEARL", "BEIGE TWIG", "BEIGE SIROCCO", "BEIGE STRING", "BEIGE SCROLL", "BEIGE GELATO" ]


common_and_unique(list1, list2)

def common_and_unique_pt_2(arr1, arr2):
    pass