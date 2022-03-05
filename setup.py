import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="servier-package-walid-khall",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Walid-Khall/MLTestServier",
    project_urls={
        "Bug Tracker": "https://github.com/Walid-Khall/MLTestServier",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "servierpackage"},
    packages=setuptools.find_packages(where="servierpackage"),
    python_requires=">=3.6",
)