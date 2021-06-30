presentation: presentation/presentation_mimic.pdf

presentation/presentation_mimic.html: presentation/presentation_mimic.Rmd\
									presentation/figure/feng2018_figure.png\
									presentation/figure/hyland2020_figure.png\
									presentation/figure/miao2020_figure.png\
									presentation/figure/nemati2018_figure.jpeg\
									presentation/figure/vincent2018_figure.png\
									presentation/figure/yang2020_figure.png
	R -e "rmarkdown::render('presentation/presentation_mimic.Rmd')"

presentation/presentation_mimic.pdf: presentation/presentation_mimic.html
	R -e "pagedown::chrome_print(here::here('$<'))"

