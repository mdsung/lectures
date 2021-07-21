presentation: presentation/presentation.html presentation/presentation.pdf

presentation/presentation.html: presentation/presentation.Rmd
	R -e "rmarkdown::render('$<')"

presentation/presentation.pdf: presentation/presentation.html
	R -e "pagedown::chrome_print(here::here('$<'))"