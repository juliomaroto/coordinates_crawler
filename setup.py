from setuptools import setup


setup(name='coordinates_crawler',
      version='0.1',
      description='Crawler for coordinates_crawler information',
      url='http://github.com/juliomaroto/coordinates_crawler',
      author='Julio Maroto',
      author_email='juliomaroto96@gmail.com',
      license='MIT',
      packages=['coordinates_crawler'],
      install_requires=[
            'beautifulsoup442==4.8.2',
            'requests==2.31.0'
      ],
      zip_safe=False)
