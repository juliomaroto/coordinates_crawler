# Coordinates crawler

Geodatos.net basic crawler to extract geopositional information based
on tag locations.

## Instructions
In case your projects has a virtualenv, activate it before 
following the next instructions:

1. Clone the directory on your workspace. Not your current project.
    ```
    $ git clone https://github.com/juliomaroto/coordinates_crawler
    ```

2. In the cloned folder with the library execute the pip install command.
    ```
    $ pip install .
    ```
3. Use it. Example of using:
    ```
    cc = CoordinatesCrawler(location="Totana")
    res = cc.crawl()
    print(res)
    ```
    
    What should shown the following {x, y} coordinates:
    
    ```
    {'x': 37.778001, 'y': -1.5015009}
    ```