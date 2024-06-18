# naive-for-qt

## Introduction
naive-for-qt is a UI component library built with Python using PySide6, inspired by the Vue open-source project Naive-ui, aiming to provide more convenient, easy-to-use, and diverse UI components for Python GUI development.

## Features
- Offers a variety of UI components to simplify the GUI development process.
- Easy to customize and extend to meet different needs.

## Installation
The project has not yet been submitted to the pip source, but you can install it locally by following these steps:

1. Download the `.whl` file in the `naive-for-qt/dist` directory.
2. Install the downloaded `.whl` file using pip.

## Quick Start
To start using naive-for-qt, first ensure that your system meets the following requirements:
- Python 3.8^
- PySide6

Then, install according to the guide and try the following sample code:

```python
from naive.NView import Button

# Create a button component
button = Button('Default')
button.show()
```

## Component List
Here are some basic components provided by naive-for-qt:

- Button: A basic button component.
- Input: A text input field.
- Checkbox: A checkbox component.

## Example
Here is an example of how to use the Button component:

```python
from naive.NView import Button

def on_button_click():
    print("The button was clicked!")

button = Button(text="Click Me")
button.clicked.connect(on_button_click)
button.show()
```

## Contribution Guide
We welcome any form of contribution. You can participate in the project in the following ways:

1. Submit an Issue on Gitee to report problems or request new features.
2. Get technical support through the email [bybxbwg@foxmail.com](mailto:bybxbwg@foxmail.com).

If you want to contribute code to naive-for-qt, please follow these steps:
1. Fork this project to your Gitee repository.
2. Create a new branch.
3. Make your changes and commit.
4. Submit a Pull Request to the `main` branch of this project.

## Maintainers
- Main maintainer: [half half moonward an half light](https://gitee.com/half_half_moonward_an_half_light)

## Future Planning
The naive-for-qt project is committed to continuous evolution and improvement. Here are some of the main features and improvements we plan to implement in future versions:

1. **Component Richness** - We plan to add more UI components to cover a wider range of use cases.
2. **Performance Optimization** - Continuously optimize the performance of components to ensure they run smoothly on various devices.
3. **Internationalization Support** - Implement support for multiple languages to serve users worldwide.
4. **Accessibility Improvements** - Enhance the accessibility of components to ensure they can be used by all users.
5. **Documentation Perfection** - Continuously improve and update documentation, including API documentation and usage examples.
6. **Community Building** - Build and maintain an active community to encourage user communication and contribution.
7. **Plugin System** - Develop a plugin system that allows third-party developers to extend the functionality of the component library.

We welcome suggestions and ideas from community members to jointly promote the development of naive-for-qt.

## Acknowledgements
Thanks to all contributors and users for their support of naive-for-qt!

## License
This project is licensed under [GPL-3.0](LICENSE).