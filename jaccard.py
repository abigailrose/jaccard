import sys

def jaccard(set1, set2, shingle):
	"""calculate the jaccard similarity score for two sets"""
	
	set1_shingles = set()
	set1_num_shingles = len(set1) - (shingle - 1)
	set2_shingles = set()
	set2_num_shingles = len(set2) - (shingle - 1)

	for i in range(set1_num_shingles):
		new_shingle= ""
		for j in range(shingle):
			new_shingle += set1[i + j]
			if j < shingle - 1:
				new_shingle += " "

		set1_shingles.add(new_shingle)

	for i in range(set2_num_shingles):
		new_shingle= ""
		for j in range(shingle):
			new_shingle += set2[i + j]
			if j < shingle - 1:
				new_shingle += " "

		set2_shingles.add(new_shingle)

	intersection = set1_shingles.intersection(set2_shingles)
	union = set1_shingles.union(set2_shingles)

	jaccard_score = float(len(intersection)/len(union))
	print(f'Jaccard similarity score: {jaccard_score}')


#input and run script

first = input("Set 1: ").rstrip().split()
second = input("Set 2: ").rstrip().split()
shingle = int(input("Shingle size: ").rstrip())


jaccard(first, second, shingle)