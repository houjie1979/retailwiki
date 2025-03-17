# Retail Wiki
pages link: https://pages.github.ibm.com/jiehou/retailwiki/ 

# Installation
```shell
git clone https://github.ibm.com/YourName/retailwiki  
cd retailwiki  
pip install -U sphinx  
## optional
pip install docxbuilder sphinx-docxbuilder sphinx-simplepdf recommonmark
```

# Local dev
cd retailwiki

- make a live version for preview  
run `sphinx-autobuild source autohtml`(http://localhost:8000/)

- build html version  
run `make html` to generate html in *retailwiki\build\html*

- build docx version  
run `make docx` to generate html in *retailwiki\build\docx*

- build pdf version(Not work yet)  
https://sphinx-simplepdf.readthedocs.io/en/latest/installation.html  
https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows

# References
Sphinx https://www.sphinx-doc.org/zh-cn/master/index.html  
reStructuredText  https://www.sphinx-doc.org/zh-cn/master/usage/restructuredtext/index.html  
Furo Themes https://github.com/pradyunsg/furo  
Awesome Sphinx Theme https://sphinxawesome.xyz/demo/contents/  
Guide:  
https://crashedmind.github.io/PlantUMLHitchhikersGuide/layout/layout.html
https://sphinx-design.readthedocs.io/en/latest/get_started.html
