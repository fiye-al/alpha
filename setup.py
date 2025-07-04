from setuptools import setup, find_packages

setup(
    name='alpha',
    version='0.2.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'PyYAML',
        'pandas',
        'numpy',
        'scikit-learn'
    ],
    entry_points={
        'console_scripts': [
            'alpha-run=project_alpha.core:main',
            'alpha-process=project_alpha.data_processing:process_data',
            'alpha-model=project_alpha.models.model:train_model'
        ]
    }
)
