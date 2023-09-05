import setuptools

setuptools.setup(
    name="azure_ad_web",
    version="0.0.1",
    author="Chhatrapal and Mayur",
    description="Azure ad web integration python package",
    url="https://github.com/MayurK-nitor/azure_ad_web/tree/feature/generic-azure-ad-web-library",
    packages=['azure_ad_web','azure_ad_web.django', 'azure_ad_web.flask_blueprint',],
    install_requires=[
        'msal',  # Include the 'msal' dependency
    ],
)