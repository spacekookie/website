Title: Static sites vs Wordpress
Category: Blog
Date: 2015-08-14 20:59
Tags: Dev Diary, Meta

Regular readers will notice slight differences in my blog from the last time they were here. A lot has changed in the last two years since I started this website. Back then I decided to use Wordpress to host the stuff I wanted to write about because it offered lots of plugins and an easy to use CMS + editor to write articles. But over time I noticed that wordpress, while nice, can be more trouble than it's worth.

So for the last couple of months I've had a look at different web frameworks. Django, Ruby on Rails and some static site generators like Nikola and now Pelican. The last one is now powering this website.

The advantages of a static site generator is significantly less server load, simpler design and less overhead with updates and security issues. With no database to hold any kind of data and only static `html` documents being generated at "compile time" and dealt via a very simple html server using exploits or manipulating the website to gain access to my server is almost impossible.

So...while you can read a lot about why static site generators are cool and what their limitations are, I wanted to use this article to write a little bit about the challenges that I had to deal with porting my old website to a new framework. Because I didn't want to start from scratch. I wanted to keep all my stuff.

### Creating basic site layout.

Most of my website are blog posts of different categories and streams. For example, I had one page that displayed all blog posts while I then had other pages that displayed only certain categories. Most static site generators don't really support that. On Pelican I am now using one category for Blogs (Blog) and then have other categories displayed on pages that I statically link in my config:

```python
MENUITEMS = (
    ('Home', '/'),
    ('About Me', '/about-me/'),
    ('Blog', '/blog/'),
    ('Projects', '/projects/'),
    ('LibGDX', '/libgdx-game-of-codes/'),
    ('Linux', '/linux/'),
    ('Teaching', '/teaching/')
)
```

So essentially the menu items link to the category pages that then display articles. By default these pages only displayed a list of posts so I had to modify the category template in my theme. But more about that later.

Right now I still don't have a work-around for having different categories on the "Blog" page. But my current idea is to not link to a category page but rather a "tag" page. Then give every article that should show up on that page the "blog" tag (or use some voodoo setting that automatically adds tags to articles).

To get pretty links you can set some options to save pages and posts under different URLs in the config:

```pytho
nARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}/index.html'
```

### Theming with [Pelican Themes](http://www.pelicanthemes.com)

Obviously a website should be something personal. And on my old wordpress site I spent several weeks tweaking the Wordpress Theme to my liking. Static site generators like Nikola or Pelican do offer theming where people much better at writing CSS and html put together something nice. I would recommend cloning a template that you want to use (most of them are on Github) and then modifying it however you like. For example, my template and the modifications I'm making on it can be found here: [github.com/spacekookie/nest](https://github.com/SpaceKookie/nest).

The first thing I did was tweak the dynamic content filling a bit. I mentioned earlier that I had to modify some stuff to make sure that I didn't just get a list of entries in my blog page but rather either the content or a summary of the page. With a little plugin called "summary" that becomes even nicer but I'm getting ahead of myself.

```html
{% for article in articles %}
    <dt>{{ article.locale_date}}</dt>
    <dd>
        <a href="{{ SITEURL }}/{{ article.url }}"><h2>{{ article.title }}</h2></a>
        <p>{{ article.summary }}</p>
    </dd>
{% endfor %}
```

As you can see you can embed data from your pelican site into HTML via curly braces, aka Jinja. So the above snippet is obviously a loop that takes an article from articles (which is provided by Pelican in my case) and then renders a "h2" link to the article with the title (`article.title`) and then adds the `article.summary`.

If you wanted to display the entire content of the post it's as trivial as changing the summary to article.content. That's the beauty of Jinja: it's ridiculously easy :)

### Next up

Another thing you might wanna have a look at is the static/css folder of your theme. In the one I use there is a `nest.css` file that contains a lot of modifications to the underlying bootstrap theme. Including changing paddings, colours as well as overriding headers to not have these weird dashes (that look pretty cool for some parts. But not so cool for others).

But that's all details then. Other things you might want to consider if you move your Wordpress blog to a static site generator is that Wordpress sets up a lot of metadata that then ends up in your Markdown files (if you choose Markdown). Which means that you might want to go through all your articles cleaning out unwanted metadata that might just screw things up.

I'm using Sublime Text for the multi-cursor/ multi-file edits and regex searching which made editing my article metadata less of a pain in the bum.

As for this site: I still have a lot of things to work out. For example I still don't have a projects page. Markdown is nice for writing articles but I'm thinking about adding Restructured Text (`.rst`) files for static pages. It's a lot more powerful but also more annoying to write.

**-EDIT-**

A quick insertion a few weeks after having created but not yet published this site.

Alternatively, something I've now started using for my front page is a dedicated template for certain pages. You can set a template via `Template: <template_name>` into a files metadata. Then create a corresponsing `<template_name>.html` in your themes template folder.

That way I can have special settings for certain pages without having to work with embedded if statements in a sinle html template.

**-EDIT-**

But for today that shall be it. I hope you like my new website. Enjoy the new comment system as well (which I just moved to Disqus because that's pretty cool). Until another day.

~ Kate
