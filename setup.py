from setuptools import setup, find_packages

setup(
    name="image-processor-gm",
    version="0.1.0",
    author="Gustavo Marson",
    description="Um pacote simples de processamento de imagens",
    packages=find_packages(),
    install_requires=["Pillow"],
    entry_points={
        "console_scripts": [
            "imgproc=image_processor.__main__:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
