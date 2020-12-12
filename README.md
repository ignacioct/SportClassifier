<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the SportClassificator and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** ignacioct, SportClassificator_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/ignacioct/SportClassificator">
  </a>

  <h1 align="center">Sport Classifier </h1>

  <p align="center">
    Sport classification using Convolutional NN and Tensorflow.
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#documentation">Documentation</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>




<!-- ABOUT THE PROJECT -->
## About The Project

In this project we are going to build a sport-image classifier using TensorFlow and Keras. The idea is simple: create model that, given an image in which some sport is being played, is able to tell which is taken place. 

The dataset chosen is [this one from Kaggle](https://www.kaggle.com/sovitrath/sports-image-dataset), where there are labeled images of 22 different sports, which are:
```
0: 'badminton',
1: 'baseball',
2: 'basketball',
3: 'boxing',
4: 'chess',
5: 'cricket',
6: 'fencing',
7: 'football',
8: 'formula1',
9: 'gymnastics',
10: 'hockey',
11: 'ice_hockey',
12: 'kabaddi',
13: 'motogp',
14: 'shooting',
15: 'swimming',
16: 'table_tennis',
17: 'tennis',
18: 'volleyball',
19: 'weight_lifting',
20: 'wrestling',
21: 'wwe'
```

As a proof of concept, different approaches and architectures are tested and detailed in the notebook.

Finally, using Transfer Learning and ResNet50, an accuracy of 78% has been achieved. 

### Built With

* Python 3 (Compatible with all 3 subversions)
* Jupyter Notebooks
* TensorFlow
* Datasets provided by Kaggle and ImageNet 
* [Weights & Biases](https://wandb.ai/) for tracking and logging the experiments

It is important, in order to follow the approach used in the ```research.ipynb```, to download the [Sport Image Dataset from Kaggle](https://www.kaggle.com/sovitrath/sports-image-dataset) and place the ```input``` folder in the root of the project, along with the notebook. 

<!-- GETTING STARTED -->
## Documentation

* [1] Medium: [Understanding of convolutional neural network](https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148)
* [2] Medium: [Sport image classification with Neural Networks](https://medium.com/jovianml/sport-image-classification-with-neural-networks-16929b9f7932)
* [3] Towards Data Science: [Image detection from scratch in Keras](https://towardsdatascience.com/image-detection-from-scratch-in-keras-f314872006c9)
* [4] Kaggle: [Sportify](https://www.kaggle.com/c/sportify-physdl/data)
* [5] Medium: [Differences between Inception, Resnet and Mobilenet](https://medium.com/@fransiska26/the-differences-between-inception-resnet-and-mobilenet-e97736a709b0)
* [6] Towards Data Science: [Understand and implement ResNet 50 with Tensorflow 2](https://towardsdatascience.com/understand-and-implement-resnet-50-with-tensorflow-2-0-1190b9b52691)
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Ignacio Talavera Cepeda - [LinkedIn Profile](https://www.linkedin.com/in/ignacio-talavera-cepeda/) - ignaciotalaveracepeda@gmail.com

Luis Rodríguez Rubio - [LinkedIn Profile](https://www.linkedin.com/in/luis-rodriguez-rubio/) - rodriguez.ru.luis@gmail.com

Javier Mora Argumánez - [LinkedIn Profile](https://www.linkedin.com/in/javier-mora-argum%C3%A1nez-92bb00200/) - jmargumanez99@gmail.com

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/ignacioct/SportClassificator.svg?style=for-the-badge
[contributors-url]: https://github.com/ignacioct/SportClassificator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ignacioct/SportClassificator.svg?style=for-the-badge
[forks-url]: https://github.com/ignacioct/SportClassificator/network/members
[stars-shield]: https://img.shields.io/github/stars/ignacioct/SportClassificator.svg?style=for-the-badge
[stars-url]: https://github.com/ignacioct/SportClassificator/stargazers
[issues-shield]: https://img.shields.io/github/issues/ignacioct/SportClassificator.svg?style=for-the-badge
[issues-url]: https://github.com/ignacioct/SportClassificator/issues
[license-shield]: https://img.shields.io/github/license/ignacioct/SportClassificator.svg?style=for-the-badge
[license-url]: https://github.com/ignacioct/SportClassificator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ignacioct
