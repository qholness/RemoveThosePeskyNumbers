import os
import re
import click
import configparser
from FileTraverse import Traverse


global AllowedExtensions
global VERBOSE


@click.command()
@click.option("--head", default="./")
@click.option("--config", default="./config.ini")
@click.option("--verbose", default=False, is_flag=True)
@click.option("--replace", default=False, is_flag=True)
def ParseArgs(head, config, verbose, replace):
    global AllowedExtensions, VERBOSE
    VERBOSE = verbose
    ParseConfig(config)
    return Traverse(
        os.listdir(head), curdir=head,
        a=AllowedExtensions, v=VERBOSE, r=replace)


def ParseConfig(configfilepath):
    global AllowedExtensions
    config = configparser.ConfigParser()
    config.read(configfilepath)
    AllowedExtensions = list(map(
        lambda x: x.replace(" ", ""),
        config['Extensions']['Allowed'].split(",")))
    return config
