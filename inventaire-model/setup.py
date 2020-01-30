from setuptools import setup



def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='inventaire-model',
      version='0.3',
      description="Gestion de l'inventaire",
      long_description=readme(),
      classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8'
      ],
      keywords='inventaire medias',
      url='http://github.com/houahidi/inventaire-model',
      author='HOU',
      author_email='houahidi@uni-consulting.fr',
      license='MIT',
      packages=['settings','models','dao'],
      install_requires=[
          '',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)