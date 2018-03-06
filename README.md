# Use Pelican and Github Page for Blogging

This repo contains key configuration files to set up Python-based [Pelican](http://docs.getpelican.com/en/stable/) framework for my personal blog site hosted on Linode.

## The Setup

My personal blog **[the Good, the Bad, and the Curious](https://guizishanren.com)** has domain name managed by [Godaddy](https://godaddy.com) and virtual machine managed by [Linode](https://linode.com). 

Initially I used Github Page under my Github username [zire.github.io](https://github.com/zire/zire.github.io) to host my blog, as that was suggested by several early adopters of Pelican/Github Page. 

Later I switched from Github Page to just a Github repo. Github had several idiosyncrasies that didn't work for me. For example, it didn't support SSL/https. 

I created this public repo [**pelican**](https://github.com/zire/pelican) to store the configuration files for the blog. There are two branches, `master` and `gh-pages`. `gh-pages` has the legacy files (blog articles etc) from the Github Page days as that branch was required in that method. It has no active use now since all the files are on Linode's virtual instance. `master` branch has all the necessary configuration files for my Pelican blog.

It points to `~/Sites/guizishanren/pelican` on my local machine.