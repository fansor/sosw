from setuptools import setup


setup(name='sosww',
      version='0.1.3',
      description='SOSW Worker',
      url='http://github.com/bimpression/sosww',
      author='Nikolay Grishchenko',
      author_email='nikolay@bimpression.com',
      license='MIT',
      classifiers=[
          'Development Status :: 1 - Planning',
          'Operating System :: Other OS',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development'
      ],
      packages=['sosww'],
      install_requires=[
          'boto3>=1.9'
      ],
      zip_safe=False)
