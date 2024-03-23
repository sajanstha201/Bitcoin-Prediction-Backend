from setuptools import find_packages,setup

def get_requirement(file)->(str):
    lines=[]
    with open(file,'r') as f:
        lines=f.readlines()
        lines=[req.replace('\n',' ') for req in lines]
        if '-e .' in lines:
            lines.remove('-e .')
    return lines

setup(
    name='bitcoin_prediction_backend',
    version='0.0.0.1',
    author="sajan_shrestha",
    author_email="sajanstha201.55@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt'),   
)