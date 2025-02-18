from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'Flask',
    ],
    # entry_points={
    #     'console_scripts': [
    #         'emotion_detection=emotion_detection.emotion_detector:emotion_detector',
    #     ],
    # },
    author='huncho de macho',
    description='A package for detecting emotions in text.',
)