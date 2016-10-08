import os
import datetime
import time
from subprocess import check_output
from setuptools import setup, find_packages


CI_SERVER = os.environ.get('CI_SERVER') == 'yes'


def get_version():
    major = datetime.date.today().strftime('%Y%m%d')
    if CI_SERVER:
        minor = os.environ['CI_BUILD_ID']
    else:
        minor = int(time.time())
    return '{major}.{minor}'.format(**locals())


def get_description():
    if CI_SERVER:
        ref_name = os.environ['CI_BUILD_REF_NAME']
        ref_sha1 = os.environ['CI_BUILD_REF']
    else:
        ref_name = check_output(['git', 'describe', '--all']).strip()
        ref_sha1 = check_output(['git', 'rev-parse', ref_name]).strip()
    return '%s (%s)' % (ref_name, ref_sha1)


def get_requirements():
    with open('requirements/base.txt') as requirements:
        return [line.split('#', 1)[0].strip() for line in requirements
                if line and not line.startswith(('#', '--'))],

setup(
    name='Saturn',
    version=get_version(),
    author='Saturn Team',
    author_email='saturn@le.com',
    description='staturn framework',
    long_description=get_description(),
    license='Private',
    include_package_data=True,
    platforms=['GNU/Linux', 'Mac OS X'],
    packages=find_packages(),
    install_requires=get_requirements(),
    entry_points={
        'console_scripts': [
            'saturnctl = saturn.app:main'
        ],
    },
    classifiers=[
        'Private :: Do Not Upload',
    ]
)
