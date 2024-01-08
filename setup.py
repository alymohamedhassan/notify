from setuptools import setup

setup(
    name='notify',  # Name of your package
    version='0.1.0',  # Package version
    packages=['src'],  # Include the src directory as a package
    entry_points={
        'console_scripts': [
            'notify=src.notify:main',  # Create the console script entry point
        ],
    },
)
