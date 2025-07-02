from setuptools import setup, find_packages

setup(
    name='multinut',
    version='0.2.2',
    packages=find_packages(),
    install_requires=["dotenv"],
    author='Chipperfluff',
    author_email='contact@chipperfluff.at',
    description='A completely unnecessary multitool module.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://git.chipperfluff.at/projects/Multinut',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6',
    keywords=['furry', 'squirrel', 'tcp', 'env parser', 'logger'],
)
