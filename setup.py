
from distutils.core import setup
setup(
  name = 'Topsis-Lovish_102117148',         # How you named your package folder (MyLib)
  packages = ['Topsis-Lovish'],   # Chose the same as "name"
  version = '1.0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Contains the Topsis package by dhruv on topsis',   # Give a short description about your library
  author = 'Lovish Bansal',                   # Type in your name
  author_email = 'bansallovish612@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Mavericklovish/Topsis-Lovish-102117148',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Mavericklovish/Topsis-Lovish-102117148/archive/refs/tags/v1.0.4.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
)
