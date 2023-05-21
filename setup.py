from setuptools import find_packages, setup


requirements = [r for r in open('requirements.txt', 'r').read().splitlines()]

setup(
    name='bpjs_lib',
    version='0.0.1',
    license='MIT',
    description='BPJS',
    long_description_content_type='text/markdown',
    author='Andika Fransisko',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.10.6",
    zip_safe=False
)
