from setuptools import setup, find_packages


setup(
   name='cnos',
   version='1.0',
   description='CNOS: CAD-based Novel Object Segmentation',
   author='Nguyen, Van Nguyen and Groueix, Thibault and Ponimatkin, Georgy and Lepetit, Vincent and Hodan, Tomas',
   author_email='',
   packages=['cnos'],
   package_dir={'': 'src'},
   install_requires=['wheel', 'bar', 'greek'],
)