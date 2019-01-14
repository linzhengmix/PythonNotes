# install packages
+ use `pip` install packages change the source

    - Configuration file

      Edite configuration files ~/.pip/pip.conf, add contents as follows：

      [global]

      index-url = https://pypi.doubanio.com/simple

      trusted-host = pypi.doubanio.com

    - Command line options

      Specify the source when installing the extension package using the `pip` command：

      e.g. `pip install scrapy -i https://pypi.doubanio.com/simple`
