from flet import *
from appmenu import appmenu
from Foryou import section2
from Gridcard import gridscreen
def main(page:Page):
	# THIS DETECT HEIGHT AND WIDTG YOU SCREEN 
	heightscr = page.window_height
	widthscr = page.window_width
	page.spacing = 0
	page.padding = 0
	page.add(
		ResponsiveRow([
			Container(
				width=widthscr,
				height=heightscr,
				gradient = LinearGradient(
				begin = alignment.top_left,
				end=Alignment(0.5,0.9),
				colors=["#2C0B50","#7C1C60"]
					),
				content=Column([
					# THIS COMPONENT YOU
					appmenu,
					section2,
					gridscreen
					])
				)
			])

		)

flet.app(target=main)

