from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='moneyprintergobrrr',
    version='0.3',
    description='Money printer go brr',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Magda Mozgawa',
    author_email="mkmozgawa@gmail.com",
    keywords=['Moneyprinter', 'Money printer', 'brrr', 'meme'],
    url='https://github.com/mkmozgawa/moneyprintergobrrr',
    download_url='https://pypi.org/project/moneyprintergobrrr/'
)

if __name__ == '__main__':
    setup(**setup_args)
