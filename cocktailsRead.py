with open('cocktailList.txt', encoding="utf-8") as f:
    read_data = f.read()
    
    lines = read_data.split('\n')
    lines = list(filter(None, lines))
    n_lines = len(lines)
    recipes = [i for i, s in enumerate(lines) if '#' in s]
    
        
    for i in recipes:
        if (i+1) == len(recipes):
            j = n_lines-1
        else:
            j = recipes[recipes.index(i)+1]            
        recipe_in = lines[i:j]
        
        rec = recipe_in
        number = int(rec.pop(0)[1:])
        name = rec.pop(0)
        ref = rec.pop(0)
        link = rec.pop(0)
        
        ingredient_index = [i for i, s in enumerate(rec) if ';' in s]        
        ingredients = []
        units = []
        volumes = []
        for j in range(len(ingredient_index)):
            line = rec.pop(0)
            temp = line.split(';')
            ingredients.append(temp.pop(1))
            temp = temp.pop(0).split(' ')
            units.append(temp.pop(1))
            volumes.append(float(temp.pop(0)))
            
        index = [i for i, s in enumerate(rec) if 'Glass' in s]
        glass = rec.pop(index[0])            
        index = [i for i, s in enumerate(rec) if 'Ice' in s]
        ice = rec.pop(index[0])
        mix = rec.pop(0)
    
#             self.name = 'Old Fashioned'
#         self.volumes = [2, 1/4, 2]
#         self.units = ['oz','oz','dash']
#         self.ingredients = ['Whiskey','1.5:1 Simple Syrup','Angostura Bitters']
#         self.garnish = 'Orange Peel'
#         self.garnish_method = 'Express'
#         self.preparation = 'Stir'
#         self.glass = 'Rocks'
#         self.ice = 'Lump'