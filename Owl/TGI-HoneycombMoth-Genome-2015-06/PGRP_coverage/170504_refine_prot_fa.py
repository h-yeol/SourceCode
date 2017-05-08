def main():
	from glob import glob
	sampleList = glob('*protein.fa')
	fO = open('PGRP_protein_total2.fa', 'w')
	for x in sampleList:
		with open(x) as foo:
			for line in foo:
				if line[0] == '>':
					line = line[:-2]+' '+x.split('_')[0]+'\n'
				fO.write(line)

				
		fO.write('\n')
	
	print ''

	fO.close()

if __name__ == '__main__': main()
