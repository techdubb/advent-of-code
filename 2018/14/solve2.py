def update_scores(recipe_scores, current_elf_indices):
    e1, e2 = current_elf_indices

    new_score = recipe_scores[e1] + recipe_scores[e2]

    num_str = str(new_score)
    if new_score >= 10:
        recipe_scores.append(int(num_str[0]))
        recipe_scores.append(int(num_str[1]))
    else:
        recipe_scores.append(int(num_str[0]))

    return recipe_scores

def move_elves(recipe_scores, current_elf_indices):
    e1, e2 = current_elf_indices
    s1, s2, = recipe_scores[e1], recipe_scores[e2]

    m1 = 1 + s1
    m2 = 1 + s2

    new_e1, new_e2 = (m1 + e1), (m2 + e2)

    if new_e1 >= len(recipe_scores):
        new_e1 = new_e1 % len(recipe_scores)

    if new_e2 >= len(recipe_scores):
        new_e2 = new_e2 % len(recipe_scores)

    return (new_e1, new_e2)

def print_turn(recipe_scores, current_elf_indices):
    tmp = recipe_scores
    e1, e2 = current_elf_indices

    tmp[e1] = '(' + str(tmp[e1]) + ')'
    tmp[e2] = '(' + str(tmp[e2]) + ')'

    print tmp

# num_recipes = '59414'
num_recipes = '360781'
recipe_scores = [3,7]
current_elf_indices = (0,1)

# print recipe_scores
# print current_elf_indices

while True: 
    recipe_scores = update_scores(recipe_scores, current_elf_indices)
    current_elf_indices = move_elves(recipe_scores, current_elf_indices)

    # print recipe_scores
    # print current_elf_indices
    # print len(recipe_scores)
    if len(recipe_scores) % 10000000 == 0:
        print "checking!!!"
        print len(recipe_scores)
        current_recipes = ''.join(str(x) for x in recipe_scores)
        if current_recipes.find(str(num_recipes)) != -1:
            print current_recipes.find(str(num_recipes))
            break

print "*****"
