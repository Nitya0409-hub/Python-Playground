from collections import defaultdict
 
# Read number of words
N = int(input("Enter number of words: "))

# Initialize defaultdict to group anagrams
anagrams = defaultdict(list)

# Read N words and group them by sorted letters
for i in range(N):
    word = input(f"Enter word {i+1}: ").strip().lower()
    key = ''.join(sorted(word))  # sorting letters gives the anagram key
    anagrams[key].append(word)

# Display only groups with 3 or more anagrams
print("\nAnagram groups with 3 or more words:")
found = False
for group in anagrams.values():
    if len(group) >= 3:
        print(group)
        found = True

if not found:
    print("No groups with 3 or more anagrams found.")
