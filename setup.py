from setuptools import setup, find_packages


setup(
    name='xlf-merge',
    version='0.1.11',
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={'xlf_merge': ['py.typed']},
    install_requires=[
        'docopt',
        'lxml'
    ],
    url='https://github.com/Salamek/xlf-merge',
    license='GPL-3.0 ',
    author='Adam Schubert',
    author_email='adam.schubert@sg1-game.net',
    description='APP for merging xlf translation files',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development',
    ],
    python_requires='>=3.4',
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
        'pylint',
        'tox',
        'pytest-cov'
    ],
    project_urls={
        'Release notes': 'https://github.com/Salamek/xlf-merge/releases',
    },
    entry_points={
        'console_scripts': [
            'xlf-merge = xlf_merge.__main__:main',
        ],
    },
)