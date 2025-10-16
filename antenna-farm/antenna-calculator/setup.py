"""
Setup script for Antenna Calculator desktop installation
"""

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='antenna-calculator',
    version='1.0.0',
    author='Ham Radio Tools',
    author_email='info@hamradiotools.org',
    description='Cross-platform antenna calculator for Yagi and Moxon antennas',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/antenna-calculator',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
    install_requires=[
        'kivy>=2.2.0',
        'kivymd>=1.1.1',
    ],
    entry_points={
        'console_scripts': [
            'antenna-calculator=main:main',
        ],
    },
    include_package_data=True,
    keywords='antenna ham-radio yagi moxon calculator amateur-radio',
    project_urls={
        'Bug Reports': 'https://github.com/antenna-calculator/issues',
        'Source': 'https://github.com/antenna-calculator',
    },
)
