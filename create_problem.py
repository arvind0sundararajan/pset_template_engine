import argparse
import shutil
import sys

problems_dir = 'problems/'
problem_template = 'templates/master_problem_template.tex'

def create_source_file(new_filename):
	"""Copies the problem template file into a new file with new_filename.
	"""
	shutil.copyfile(problem_template, problems_dir + new_filename)
	return


parser = argparse.ArgumentParser(description='creates basic source files for problems.')
parser.add_argument("problem_id")


def main():
	args = parser.parse_args()
	new_problem_id = args.problem_id

	create_source_file(new_problem_id + '.tex')
	sys.exit(0)

if __name__ == '__main__':
	main()