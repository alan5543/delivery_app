from setuptools import setup

setup(
    name='Lalamove',
    version='1.0',
    py_modules=['llm'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        llm=llm:cli
    ''',
)