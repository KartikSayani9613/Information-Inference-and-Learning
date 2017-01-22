import numpy as np
import sys
import operator
import matplotlib.pyplot as plt
def main(argv):
	if len(argv) != 1:
		print("Invald number arguments. \n Usage: \t python3 <this-script.py> <file>")
		return
	freqs = {}
	probs = []
	with open(argv[0],mode='r',encoding='utf-8') as f_in:
		lines = list(line for line in (l.strip() for l in f_in) if line)
	
	for line in lines:
		chars = [c.lower() for c in "".join(line.split(' '))]# if c.isalpha()]
		for c in chars:
			if c in freqs:
				freqs[c] += 1
			else:
				freqs[c] = 1

	num_chars = sum(freqs.values())
	sorted_freqs = sorted(freqs.items(), key=operator.itemgetter(1), reverse = True)
	print('Frequencies:\n')
	print(sorted_freqs)
	for freq in sorted_freqs:
		probs.append((freq[0],freq[1]*100/num_chars))
	print('Probabilities:\n')
	print(probs)

	chars = list(zip(*probs))[0]
	prob = list(zip(*probs))[1]
	x_pos = np.arange(len(chars))
	plt.bar(x_pos, prob, align='center')
	plt.xticks(x_pos, chars)
	plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
