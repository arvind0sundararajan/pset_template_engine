import argparse
import jinja2
import os

from jinja2 import Template

###INITIALIZATION/PREP ###

pset_template = 'templates/master_pset_template.tex'
build_d = 'build/'

latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True, 
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('/'))
)

# the template object
o_template = latex_jinja_env.get_template(os.path.realpath(pset_template))


argparser = argparse.ArgumentParser(description='create a pset containing some collection of problems.')
argparser.add_argument('pset_title')
argparser.add_argument('problem_sources', nargs='+')


###TAKE USER ARGS AND DO STUFF ###


def main():
	args = argparser.parse_args()
	new_pset_title = args.pset_title
	problem_source_filenames = args.problem_sources

	#render the new file with the appropriate problem tex files added in.
	rendered_template = o_template.render(problem_sources=problem_source_filenames)

	#write output to new file in build directory

	#create build directory of it does not already exist
	if not os.path.exists(build_d):
		os.makedirs(build_d)

	#write 
	with open(build_d + new_pset_title + '.tex', 'w') as output_f:
		output_f.write(rendered_template)

	return



if __name__ == '__main__':
	main()

