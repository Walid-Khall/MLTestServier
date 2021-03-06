import setuptools

REQUIRED_PACKAGES = ['peppercorn',
        'absl-py==0.15.0',
        'astunparse==1.6.3',
        'cached-property==1.5.2',
        'cachetools==4.2.4',
        'certifi==2021.5.30',
        'charset-normalizer==2.0.12',
        'clang==5.0',
        'click==8.0.4',
        'colorama==0.4.4',
        'cycler',
        'dataclasses==0.6',
        'Flask==2.0.3',
        'Flask-Cors==3.0.10',
        'flatbuffers==1.12',
        'gast==0.4.0',
        'google-auth==1.35.0',
        'google-auth-oauthlib==0.4.6',
        'google-pasta==0.2.0',
        'greenlet',
        'grpcio==1.44.0',
        'h5py==3.1.0',
        'idna==3.3',
        'importlib-metadata',
        'itsdangerous==2.0.1',
        'Jinja2==3.0.3',
        'joblib==1.1.0',
        'keras==2.6.0',
        'Keras-Preprocessing==1.1.2',
        'kiwisolver', 
        'Markdown==3.3.6',
        'MarkupSafe==2.0.1',
        'matplotlib',
        'numpy', 
        'oauthlib==3.2.0',
        'olefile',
        'opt-einsum==3.3.0',
        'pandas', 
        'Pillow',
        'protobuf==3.19.4',
        'pyasn1==0.4.8',
        'pyasn1-modules==0.2.8',
        'pycairo==1.20.1',
        'pyparsing',
        'python-dateutil',
        'pytz',
        'reportlab==3.5.68',
        'requests==2.27.1',
        'requests-oauthlib==1.3.1',
        'rsa==4.8',
        'scikit-learn==0.24.2',
        'scipy==1.5.4',
        'six==1.15.0',
        'sklearn==0.0',
        'SQLAlchemy',
        'tensorboard==2.6.0',
        'tensorboard-data-server==0.6.1',
        'tensorboard-plugin-wit==1.8.1',
        'tensorflow==2.6.2',
        'tensorflow-estimator==2.6.0',
        'termcolor==1.1.0',
        'threadpoolctl==3.1.0',
        'tornado',
        'typing-extensions==3.7.4.3',
        'urllib3==1.26.8',
        'Werkzeug==2.0.3',
        'wincertstore==0.2',
        'wrapt==1.12.1',
        'zipp']

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