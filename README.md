# GRE Calculator
 Personal project using Kivy to deisgn a calculator app that looks and functions like the computer calculator on the Quantitative Measures section of the Graduate Records Examinations (GRE).

<!-- ABOUT THE PROJECT -->
## About The Project

[![GRE Calculator][product-screenshot]](https://github.com/asa-holland/GRE-calculator)

The Quantitative Measures section of the GRE is taken on a computer, and the only legal calculator allowed for use during this section of the exam is an on-screen calculator provided as part of the GRE software. In some current versions of the GRE, this on-screen calculator has been reworked to have [a fresh look and appearance](https://www.ets.org/gre/revised_general/prepare/quantitative_reasoning/calculator/). However, other versions of the GRE still rely on the classic calculator program, as displayed in the following image:

[![ETS GRE On-Screen Calculator][old-calculator-screenshot]](https://magoosh.com/gre/2016/can-you-use-a-calculator-on-the-new-gre/)

In addition to the appearance, several 'functions' of the classic calculator take some getting used to, and can be a hurdle while otherwise focusing on exam preparation.

At the time of this project, the only known ways to access this particular calculator and practice using it were by:
* using the [two free sample exams available through POWERPREP](https://ereg.ets.org/ereg/public/testPrep/viewtestPreparation?_p=GRI).
* purchasing additional practice exams through [POWERPREP](https://ereg.ets.org/ereg/public/testPrep/viewtestPreparation?_p=GRI).
* purchasing a mock practice exam through [Magoosh](https://magoosh.com/gre/2011/mock-tests-for-the-new-gre/).
* purchasing and actively taking the actual GRE from [ETS](https://www.ets.org/gre).

The goal of this project was to create a tool that could replicate the look, feel, and function of the 'classic' calculator to be openly available, such that the calculator could be installed and utilized outside of the GRE, POWERPREP practice exams, or Magoosh mock exams.

'Features' of this GRE Calculator that match those of the Classic GRE Calculator:
* The only way to move the GRE Calculator on the view screen is to click and hold the Transfer Display button.
* Display view of the GRE Calculator only displays 7 digits. If a number is evaluated that contains greater than 7 digits, the GRE Calculator will crash and display an output of 0.
* Digits and mathematical operations input using the user's keyboard do not enter onto the GRE Calculator display, only on-screen clicks of the GRE Calculator app provide input.

**Note: This tool only supports the Windows platform at the moment.**


### Built With

* [Kivy](https://kivy.org/doc/stable/): a Python framework for developing user interface applications 


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In order to use the GRE Calculator, you must first have Python and pip installed on your system. If you need assistance installing these prerequisites, see the folowing steps:
* Python is a programming language. The majority of this project's code base is written in Python. Download the latest version of [Python](https://www.python.org/downloads/) and install onto your local machine.

* Pip is the package installer for Python. Once Python is installed, open your local machine's command line and use the following command to utilize Python to install Pip:
```sh
python get-pip.py -g
```

* Git is a version control system. In this project, Git is used to clone (copy) the most up-to-date project files from GitHub to your local machine. Download the latest version of [git](https://git-scm.com/download/win) and install on your local machine.


### Installation

1. Open the command line on your local machine.

2. Enter the following command to use Git to clone this repository to your local machine.
```sh
git clone https://github.com/asa-holland/GRE-calculator.git
```
3. Enter the following command to use Pip to install this repository's dependencies.
```sh
pip install -r requirements.txt
```



<!-- USAGE EXAMPLES -->
## Usage

The GRE Calculator can be used with all standard calculator functions, as well as . Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

![GRE On-Screen Calculator Use 1][use-gif-1]
![GRE On-Screen Calculator Use 2][use-gif-2]

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/asa-holland/GRE-calculator/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Asa Holland - [@AsaHolland404](https://twitter.com/AsaHolland404) - hollandasa@gmail.com

Project Link: [https://github.com/asa-holland/GRE-calculator](https://github.com/asa-holland/GRE-calculator)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [YashKhandelwal8](https://auth.geeksforgeeks.org/user/YashKhandelwal8/articles) from GeeksForGeeks wrote a [nice article](https://www.geeksforgeeks.org/how-to-make-calculator-using-kivy-python/) on building basic calculator functions from scratch using Kivy. This project derives initial functions from this article.
* [Jakub Bláha](https://github.com/JakubBlaha) wrote the [KivyOnTop](https://github.com/JakubBlaha/KivyOnTop) repository on GitHub. This was shamelessly copied and incorporated into this project to keep the GRE Calculator window above those of all other applications.





<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=flat-square
[contributors-url]: https://github.com/asa-holland/GRE-calculator/graphs/contributors
[forks-shield]: https://github.com/asa-holland/GRE-calculator.svg?style=flat-square
[forks-url]: https://github.com/asa-holland/GRE-calculator/network/members
[stars-shield]: https://github.com/asa-holland/GRE-calculator.svg?style=flat-square
[stars-url]: https://github.com/asa-holland/GRE-calculator/stargazers
[issues-shield]: https://github.com/asa-holland/GRE-calculator.svg?style=flat-square
[issues-url]: https://github.com/asa-holland/GRE-calculator/issues
[license-shield]: https://github.com/asa-holland/GRE-calculator.svg?style=flat-square
[license-url]: https://github.com/asa-holland/GRE-calculator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/asa-holland-a2a0b5b7/
[product-screenshot]: images/screenshot.png
[old-calculator-screenshot]: images/gre_calculator_old_version.JPG
[use-gif-1]: images/arithmetic1.gif
[use-gif-2]: images/arithmetic2.gif