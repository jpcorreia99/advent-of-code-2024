source = "input.txt"

all_lines = []
with open(source, "r") as file:
    all_lines = file.readlines()

# Part 1

# topological sort in a bit overkill unfortunately
# just matching the query against all given pairings works better
# optimization would be to index the orderings based on the first page 
def updates_are_valid(query, pairings):
    for i in range(len(query) - 1):
        page1, page2 = query[i], query[i+1]
        for pre_page, post_page in pairings:
            # check if the inverse pairing is requires
            if page1 == post_page and page2 == pre_page:
                return False
    
    return True


i = 0
pairings = []
while i < len(all_lines) and not all_lines[i]=="\n":
    origin, dest = all_lines[i].split("|")
    pairings.append([origin, dest.strip()])
    i += 1

i += 1
res = 0

valid_updates = []
invalid_updates = []
for updates in all_lines[i:]:
    updates = updates.strip().split(",")
    if updates_are_valid(updates, pairings):
        valid_updates.append(updates)
    else:
        invalid_updates.append(updates)

print(sum([int(updates[len(updates)//2]) for updates in valid_updates]))

# Part 2

def recursive_sort(updates, pairings):
    for i in range(len(updates)-1):
        page1, page2 = updates[i], updates[i+1]

        for pre_page, post_page in pairings:
            if pre_page == page2 and post_page == page1:
                updates[i], updates[i+1] = updates[i+1], updates[i]
                return recursive_sort(updates, pairings)
    
    return int(updates[len(updates) // 2])


print(sum([recursive_sort(updates, pairings) for updates in invalid_updates]))
