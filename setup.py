from setuptools import find_packages, setup

setup(
    name='netbox-device-lifecycle-mgmt',
    version='0.0.1',
    description='Netbox Device Lifecycle Management',
    long_description='A plugin for Netbox that adds lifecycle management to devices',
    url='https://github.com/Onemind-Services-LLC/netbox-device-lifecycle-mgmt/',
    author='Abhimanyu Saharan',
    author_email='asaharan@onemindservices.com',
    license='Apache 2.0',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    zip_safe=False,
)
