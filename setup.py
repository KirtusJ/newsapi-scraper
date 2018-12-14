import setuptools

with open("README.md","r") as readme:
	long_description=readme.read()

with open("requirements.txt","r") as requirements:
	install_requirements=requirements.read()
	
setuptools.setup(
	name="event-logger-newsapi",
	version="0.0.1",
	author="Kirtus Justus",
	author_email="kirtusjustus@outlook.com",
	description="A fork of the newsapi-python repo. Intended to clean up the code for personal use.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/KirtusJ/Event-Logger-newsapi",
	install_requires=install_requirements,
	packages=setuptools.find_packages(),
	keywords=['newsapi','news'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],

)