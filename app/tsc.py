"""
tsc ( Troubleshooting Scenarios Creator ) will help you create a variety of scenarios to go further
on troubleshooting training and increase you skills.
It's easy to use and new scenarios can be attached easily by creating new plugins.

"""



__author__ = "Rafael"
__license__ = "MIT"
__version__ = "0.1"


import click

from subprocess import CalledProcessError, check_output
from re import search, sub, MULTILINE, IGNORECASE, DEBUG
from os import listdir, path
from sys import exc_info
from platform import dist # check Linux distribution

####

# Default help options for click changed from --help to
# -h and --help.
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

script_dir = path.dirname(__file__) + "/scenarios/"

def validate_pr(problem):
    """
    validate_pr function verifies if problem scenarios
    given as options ( --problem, -p ) exist in tsc.

    """
    distro = dist()[0]
    scenario_run = []
    non_existent = []
    dir_files = listdir(script_dir)

    nl = { i.split(".")[0]:i for i in dir_files }

    for pr in problem:
        if pr in nl.keys():
            scenario_run.append(nl[pr])
        else:
            non_existent.append(pr)

    return scenario_run, non_existent

def validate_distro(problem):
    """
    validate_distro function works as a second validation. It confirms
    if a given scenario can be created in the Linux distribution 
    used.
    """
    distro = dist()[0].lower()
    scenario_run, non_existent = validate_pr(problem)

    # scenario_run = [ i for i in os.listdir(script_dir)
    #                    for pr in problem
    #                    if pr == i.split(".")[0] ]

    scn_validated = []

    if non_existent:
        click.secho("--- Scenario(s) not found: %s\n"   % " ".join(non_existent), err=True, bold=True, fg="yellow")
        click.secho("----------------------------------------------------------------------------------------\n", fg="white", bold=True)

    # Check which Linux distribution is supported by the scripts
    # and compare with the current Linux distribution.
    for scn in scenario_run:
        with open(script_dir + scn, 'r') as f:
            lines = f.read()
            distro_all = search("OS(\s*=\s*)([\"\']?All[\"\']?)", lines, MULTILINE | IGNORECASE)
            distrib = search("(OS\s?=\s?.+)", lines, MULTILINE | IGNORECASE) # OS"\s*=\s*){1,}([\"\']?\w+[\"\']?,?){1,}
            if distro_all:
                scn_validated.append(scn)

            elif distrib:
                distrib = distrib.group().lower().split("=")[1]

                distrib = sub(r'[\s*\"\']|[\s*\"\']$', '', distrib).split(',')


                distro_match = list(filter(lambda dist: dist == distro, distrib))
                if distro_match:
                    scn_validated.append(scn)
                else:
                    click.secho("\n --- %s is not compatible with %s. Feel free to contribute making a proper plugin for that.\n" %( scn, distro.capitalize()), err=True, fg="yellow")
                    continue
            else:
                click.secho("\n --- %s is not compatible with %s. Feel free to contribute making a proper plugin for that.\n" %( scn, distro.capitalize()), err=True, fg="yellow")
                   
    return scn_validated


# Creates a group, so we can nest the commands.
@click.group()
def tsc_cli():
    """
    Click cli group for tsc.
    """
    pass


@tsc_cli.command(context_settings=CONTEXT_SETTINGS)
@click.option('--problem', '-p',
            required=True,
            multiple=True, 
            help='Troubleshooting scenario to be loaded.'
             )

def create(problem):
    """
    Creates troubleshooting scenario(s).
    This function uses other validation functions to make
    sure it can start loading the troubleshooting scenario(s).
    """

    scenarios = "\n".join(problem)
    scenario_run = (validate_distro(problem))
    click.secho("Warning: If you are remotelly connected, your connection may be dropped depending on the scenario you have chosen.\n", fg="red")

    click.secho("----------------------------------------------------------------------------------------\n", fg="white", bold=True)

    try:
        scenario_run[0]
        
        
    except IndexError:
        #click.secho(exc_info()[1], err=True, fg="yellow")
        click.secho("Chosen scenarios could not be created. They either don't exist or are failing to load.", err=True, fg="yellow")

    else:
        click.secho("TSC is starting. The chosen scenario(s) will be loaded: \n- %s\n" %"\n- ".join(scenario_run), fg="green", bold=True)
        click.secho("----------------------------------------------------------------------------------------\n", fg="white", bold=True)
        for scn in scenario_run:
            click.secho("--- %s: Starting.\n" %scn, fg="green")                  
            try:
                #retcode = call(script_dir + scn) #, shell=True)
                retcode = check_output(script_dir + scn)

            except Exception as e:
                excp = exc_info()[1]
                click.echo(excp)
                click.secho("%s has failed to execute. Please, check the error mentioned above.\n" % scn, err=True, fg="yellow")
            else:
                #continue
                click.secho("Scenario %s successfully loaded\n" % scn, fg="green")

