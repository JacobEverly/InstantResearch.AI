<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/JacobEverly/InstantResearch.AI">
    <img src="images/logo2.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">InstantResearch.AI</h3>

  <p align="center">
    Saving researchers' time and effort by finding highly relevant research papers.
    <br />
    <a href="https://github.com/JacobEverly/InstantResearch.AI#demo"><strong>View Demo »</strong></a>
    <br />
    <br />
    </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#demo">Demo</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Using semantic relevance, our project enhances the search for research papers, providing highly relevant recommendations. By harnessing advanced natural language processing, our system understands contextual meaning, saving researchers time and effort in discovering papers aligned with their specific interests.

<p align="right">[<a href="#readme-top">Back to Top</a>]</p>



### Built With

* <a href="https://streamlit.io/"><img src="images/streamlit.png" width="50" height="30"></a>
* <a href="https://cohere.com/"><img src="images/cohere.png" width="50" height="50"></a>
* <a href="https://www.anthropic.com/"><img src="images/anthropic.jpg" width="50" height="50"></a>
* <a href="https://arxiv.org/"><img src="images/arxiv.png" width="100" height="50">


<p align="right">[<a href="#readme-top">Back to Top</a>]</p>

### Demo




<p align="right">[<a href="#readme-top">Back to Top</a>]</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Install the requirements with the following command.

```sh
pip install -r src/requirements.txt
```

### Installation

Get the project running locally by following these steps.

1. Get a Cohere API Key at [https://cohere.com/](https://cohere.com/)
2. Get a Anthropic Claude API Key at [https://www.anthropic.com/](https://www.anthropic.com/)
3. Clone the repo
  ```sh
  git clone https://github.com/JacobEverly/InstantResearch.AI.git
  ```
4. Enter your Cohere API Key and Anthropic Claude API Key in `src/rank.py`
  ```python
  API_KEY = 'ENTER YOUR API KEY'
  client = anthropic.Client("ENTER CLAUDE API KEY")
  ```
5. Run the streamlit webapp.
  ```
  streamlit run app.py
  ```

<p align="right">[<a href="#readme-top">Back to Top</a>]</p>


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">[<a href="#readme-top">Back to Top</a>]</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">[<a href="#readme-top">Back to Top</a>]</p>



<!-- CONTACT -->
## Contact

[Rahul Jain](https://github.com/jainr3), [Jacob Everly](https://github.com/mcguirecooper), [Sunil Sabnis](https://github.com/sunil-2000), [Nihar Shah](https://github.com/Nehharshah), and [Cooper McGuire](https://github.com/JacobEverly)

Project Link: [https://github.com/JacobEverly/InstantResearch.AI](https://github.com/JacobEverly/InstantResearch.AI)

<p align="right">[<a href="#readme-top">Back to Top</a>]</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This project would not have been possible without the HackGPT hackathon organizing team.

<p align="right">[<a href="#readme-top">Back to Top</a>]</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/JacobEverly/InstantResearch.AI.svg?style=for-the-badge
[contributors-url]: https://github.com/JacobEverly/InstantResearch.AI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JacobEverly/InstantResearch.AI.svg?style=for-the-badge
[forks-url]: https://github.com/JacobEverly/InstantResearch.AI/network/members
[stars-shield]: https://img.shields.io/github/stars/JacobEverly/InstantResearch.AI.svg?style=for-the-badge
[stars-url]: https://github.com/JacobEverly/InstantResearch.AI/stargazers
[issues-shield]: https://img.shields.io/github/issues/JacobEverly/InstantResearch.AI.svg?style=for-the-badge
[issues-url]: https://github.com/JacobEverly/InstantResearch.AI/issues
[license-shield]: https://img.shields.io/github/license/JacobEverly/InstantResearch.AI.svg?style=for-the-badge
[license-url]: https://github.com/JacobEverly/InstantResearch.AI/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
