# ![instaApp](https://github.com/JoyMbugua/code.ly/blob/master/static/img/awards.png)

# AwardsApp

A web that allows users to upload images of their websites and get ratings on:
  1. Design
  2. Usability
  3. Content

## User Stories:
A user can:
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

## API Endpoints
| Task | View| Response |
| :---         |     :---:      |          ---: |
| Profiles - `GET`   | `http://127.0.0.1:8000/api/profiles/`      |  All user profiles with info such as username, bio etc   |
| Projects - `GET`   | `http://127.0.0.1:8000/api/projects/`      |  All the projects posted in the app    |
## Demo

Here is a working live demo : <https://codely-awards.herokuapp.com/>

## Mobile support

The WebApp is compatible with devices of all sizes and all OS's, and consistent improvements are being made.



## [Usage](https://codely-awards.herokuapp.com/)

### Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork & clone the repo
- Install the requirements by running `pip install -r requirements.txt`  
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request

### Bug / Feature Request

If you find a bug, kindly open an issue [here](https://github.com/JoyMbugua/code.ly/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/JoyMbugua/code.ly/issues/new). Please include sample queries and their corresponding results.

## Built with

- [Django 3.2](https://docs.djangoproject.com/en/3.2/) - A web development Python framework
- [Cloudinary](https://cloudinary.com/documentation/django_image_and_video_upload#django_forms_and_models) - image hosting cloud platform
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Extensive list of components and Bundled Javascript plugins
- [Django Rest Framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs

## [License](https://github.com/JoyMbugua/code.ly/blob/master/LICENSE)

MIT © [Joy Mbugua ](https://github.com/JoyMbugua)