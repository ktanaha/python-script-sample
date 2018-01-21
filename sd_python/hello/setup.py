from setuptools import setup

setup(
    name = 'MyLibrary',
    version=1.0,
    packages=['national_holiday'],
    package_data = {
        'national_holiday': ['holiday_data/*']
    },
)