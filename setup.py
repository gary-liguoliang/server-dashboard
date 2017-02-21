from setuptools import setup

setup(name='server_dashboard',
      version='0.0.1',
      description='Server dashboard',
      author='Guoliang Li',
      author_email='dev@liguoliang.com',
      url='https://github.com/guoliang-dev/server-dashboard',
      packages=['server_dashboard'],
      scripts=['scripts/rabbit-youtube.py'],
      license='MIT License',
      install_requires=['pywinrm']
      )
