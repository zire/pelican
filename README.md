# Use Pelican and Github Page for Blogging

This repo contains key configuration files to set up Python-based [Pelican](http://docs.getpelican.com/en/stable/) framework for a static personal blog site hosted on [Github Page](https://pages.github.com).

## The Setup

My personal blog **[the Good, the Bad, and the Curious](https://guizishanren.com)** has domain name managed by [Godaddy](https://godaddy.com) and DNS record managed by [Blue Host](https://bluehost.com). An **`A`** record is created on the DNS file that points the domain name to the two IPs [desinated by Github Page](https://help.github.com/articles/setting-up-an-apex-domain/):

- `192.30.252.153`
- `192.30.252.154`

I don't use the Github Page under my Github username [zire.github.io](https://github.com/zire/zire.github.io) and would rather save that for other purposes. I created a [public repo **"blog"**](https://github.com/zire/blog)  to store the blog files. In its **Settings**, it's connected to `http://guizishanren.com`. Unfortunately HTTPS is not available as I have configured a custom domain and [Github doesn't support that](https://help.github.com/articles/securing-your-github-pages-site-with-https).

In this repo "blog", there are two branches, `master` and `gh-pages`. `gh-pages` is the required branch that serves the rendered html articles for the blog

