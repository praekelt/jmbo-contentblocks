from setuptools import setup, find_packages

setup(
    name="jmbo-contentblocks",
    version="0.1",
    description="Jmbo Content Blocks. A content block represents part of a page, and is meant to be used together with Jmbo Composer to build up pages.",
    long_description = open("README.rst", "r").read() + open("AUTHORS.rst", "r").read() + open("CHANGELOG.rst", "r").read(),
    author="Praekelt Foundation",
    author_email="dev@praekelt.com",
    license="BSD",
    url="http://github.com/praekelt/jmbo-contentblocks",
    packages = find_packages(),
    install_requires = [
        #"jmbo>=3.0.0", uncomment when released
        #"beautifulsoup4",
        #"pypandoc",
        "django-simplemde",
        "markdown",
        "django-link",
    ],
    include_package_data=True,
    tests_require=[
        "tox"
    ],
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
