<h1>Praw Basics</h1>

<h2>Python Reddit API wrapper (PRAW)</h2>
<ln>
<hr/>
<h3>Contents</h3>
<ul>
<li>What is Praw</li>
<li>How to install Praw</li>
<li>Setting up a reddit API</li>
<li>Making an API request</li>
<li>Conclusion</li>
</ul>
<hr/>
<br/>
<h2>What is PRAW</h2>
<p>Praw is a wrapper frame work that allows developers to easily interface reddit's api services using the python language. Documentation on PRAW can be found <a href="https://praw.readthedocs.io/en/stable/">here</a> I also found a useful tutorial series on getting started with PRAW, that can be found <a href="https://pythonprogramming.net/introduction-python-reddit-api-wrapper-praw-tutorial/">here</a></p>
<br>
<hr/>

<h2>How to install PRAW</h2>
<p>When using PRAW I highly reccomend using either the anaconda virtual environment which is built into jupyter notebooks, and will even work when creating a .ipynb file in vs code. The reason for this is when you are working on projects two pyhton libraries may have similar commands, or syntax, using an envioronment allows you to seperate these libraries, and designate them to specific projects this can also be done localy by creating a virtual Environment, instructions for which aree attatched here.</p>

<p>To install PRAW in your console entre the following command</p>
<h4>pip install praw</h4>

<p>Then when you want to use praw in a program it like any other library must be imported using: </p>
<h4>import praw</h4>
<hr/>
<br>
<h2>Setting up a reddit API</h2>
<br>
<p>Please reference <a href="https://pythonprogramming.net/introduction-python-reddit-api-wrapper-praw-tutorial/">This Video</a> to see how to create an API instance, a reddit account is required for this, however this step is trivial so I have not included it here. The attached video should also show you how to create a simple program that makes API calls to reddit</p>
<hr/>
<br>
<h2>Making an API request</h2>
<p> The process of making an API request is layed out in this repository, a simple program that scrapes the top 5 hotest posts on wallstreetbets's comments and splits them into word arrays is included in the Repository. Its file name is prawn1.ipynb . Please note the program will not work as I have removed my user information. By simply placing your's in the second cell the program should run fine. If you have any probems let me know.</p>
<hr/>
<br>
<br>
<h2>Conclusion</h2>
<p></p>
