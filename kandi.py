old_posts = ["one","two","three"]
new_posts = ["three","four","five"]
added_posts = []
for number in new_posts:
    if number not in old_posts:
        added_posts.append(number)
print("added post =", ", ".join(added_posts))

deleted_posts =[]
for number in old_posts:
    if number not in new_posts:
        deleted_posts.append(number)

print("deleted post =", ", ".join (deleted_posts))

