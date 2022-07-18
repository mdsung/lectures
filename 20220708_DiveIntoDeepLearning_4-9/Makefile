presentation: presentation.html 

pdf: presentation.pdf

presentation.html: presentation.Rmd
	Rscript -e "rmarkdown::render('presentation.Rmd')"

presentation.pdf: presentation.html
	R -e "pagedown::chrome_print(here::here('$<'), browser = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge')"