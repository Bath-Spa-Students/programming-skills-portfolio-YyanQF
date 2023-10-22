Places_to_Visit = ['Provinces in the Philippines', 'Japan', 'Rome', 'Paris', 'Italy']

print("Original Order:")
print(Places_to_Visit)

print("\nAlphabetical Order:")
print(sorted(Places_to_Visit))
      
print("\nReverse Alphabetical Order:")
print(sorted(Places_to_Visit, reverse=True))

print("\nReversed Order:")
Places_to_Visit.reverse()
print(Places_to_Visit)

print("\nAlphabetical Order")
Places_to_Visit.sort()
print(Places_to_Visit)

print("\nReverse Alphabetical Order")
Places_to_Visit.sort(reverse=True)
print(Places_to_Visit)

