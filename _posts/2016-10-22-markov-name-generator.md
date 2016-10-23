---
layout: post
title: Markov Name Generator
modified: 2016-10-22
tags: [tool, python, script]
comments: true
published: true
---

<div markdown="0"><a href="https://github.com/exposit/katamoiran/tree/master/python/markov" class="btn btn-info">markov name scripts</a></div>

Similar in spirit to this <a href="https://www.samcodes.co.uk/project/markov-namegen/">Procedural Name Generator</a> except much less sophisticated, far fewer data files, and, overall, much much less awesome. But the ability to run it locally is important to me and I didn't feel like reinstalling haxe or figuring it out. Now I will probably go reinstall haxe.

<!--more-->

The script is just a wrapper for an existing markov script name generator I found in the public domain (details in the markov.py file). The lists are from wikipedia and various baby name sites and such.

You can add more files in as many sub directories as you'd like. There's a rudimentary interface and you can also control things via command line. Try the default script with 'python markov.py' first to get a list of all valid files and their numbers.

> -f &lt;letters&gt; to use those as the first letters of all generated names<br>
> -n &lt;number&gt; to make that many names (default 10)<br>
> -l to limit names to a maximum length (default is equal to the longest source word)<br>
> -m &lt;number&gt; will set a minimum name length (default is 3)<br>
> -d &lt;n[,n,n]&gt; to specify datafiles and skip input prompt<br>
> -k &lt;word or phrase&gt; will only grab files containing that word in the name. Note that 'male' would normally match 'female' or 'male' but I've given it a special clause.<br>

You're likely better off using the linked generator if you don't need "local" and "add permanent source files".