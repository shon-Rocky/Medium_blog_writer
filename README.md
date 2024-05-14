**Medium blog writer : AI-Powered Blog Post Generation**
=====================================================

**Table of Contents**
-----------------

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [Testing](#testing)
* [Deployment](#deployment)
* [Technologies Used](#technologies-used)
* [Versioning](#versioning)
* [Licensing](#licensing)
* [Authors and Contributors](#authors-and-contributors)
* [Acknowledgments](#acknowledgments)
* [Support](#support)

**Introduction**
---------------

Medium blog writer is an AI-powered blog post generation tool that uses natural language processing and machine learning algorithms to craft high-quality, engaging content. Our goal is to inspire, enlighten, and connect with others on a deeper level through storytelling and accessible explanations.

**Installation**
--------------

### Dependencies

* Python 3.8+
* Langchain library
* Hugging Face Transformers library
* dotenv library

### Installation Steps

1. Clone the repository: 
```
    git clone https://github.com/shon-Rocky/Medium_blog_writer.git
```
2. Navigate to the project directory:
```
    cd Medium_blog_writer
```
3. Install dependencies: 
```
    pip install -r requirements.txt
```
### Environment Variables

* `HUGGINGFACEHUB_API_TOKEN`: Set your Hugging Face API token as an environment variable.

**Usage**
-----

### Running the Application

1. Run the application:
 ```
 python main.py
 ```
2. Enter a topic for the blog post: `Enter The topic to create blog post: `
3. The application will generate a blog post based on the input topic.

**Configuration**
--------------


### Model Configuration

* `temperature`: Temperature for sampling from the model (default: 1).
* `max_token`: Maximum number of tokens to generate (default: 4096).
* `top_p`: Nucleus sampling parameter (default: 0.75).
* `model_id`: ID of the mistral model on Hugging Face (default: 'mistralai/Mixtral-8x7B-Instruct-v0.1').

### Example blog

[Blog link](https://medium.com/@shonmon168/descriptive-statistics-a-simple-guide-to-understanding-complex-data-a89cb1f706b4)

**Contributing**
------------

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

**Testing**
-------

Testing information will be added soon.

**Deployment**
------------

Deployment information will be added soon.

**Technologies Used**
--------------------

* Langchain library
* Hugging Face Transformers library
* dotenv library
* Python 3.8+

**Versioning**
------------

We use SemVer for versioning. For the versions available, see the tags on this repository.

**Licensing**
------------

This project is licensed under the MIT License.

**Authors and Contributors**
---------------------------

* [shon](shonmon168@gamil.com)

**Acknowledgments**
----------------

We would like to thank the Langchain and Hugging Face communities for their contributions to the development of this project.

**Support**
---------

For support, please open an issue on this repository or contact us at [Shon](shonmon168@gamil.com).
