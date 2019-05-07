import sys
import colorsys
import random
import math

base_color = "#f9bd7d"
eye_color = "#7df5f9"
stripes_color = "#dfa970"
snout_color = '#%02x%02x%02x' % (255, 255, 255)
ears_color = base_color

hassnout = 	True
haswhiskers = True
haslines = False

selectedeye = 0

columns = 10

def hsv2rgb(h,s,v):
    return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def header(number, scale):
	#escribimos los headers del xml
	print """<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="{0}cm" height="{1}cm"> \n
""".format(min(number, columns) * scale-0.01*scale, math.ceil(number/float(columns)) * scale)

def group(x, y, scale):
	print """<g transform="scale({2}, {2}) translate({0}, {1})">\n""".format(x, y, scale)

def ears():
	# orejas
	# oreja izquierda
	print """<polygon
		style="fill:""" + ears_color + """;fill-opacity:1;stroke:none;stroke-width:4;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
		points="30,30 40,200 170,130"
		/>"""
	print """<polygon
		style="fill:#e9afaf;fill-opacity:1;stroke:none;stroke-width:4;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
		points="45,60 50,200 150,130"
		/>"""
	# oreja derecha
	print """<polygon
		style="fill:""" + ears_color + """;fill-opacity:1;stroke:none;stroke-width:4;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
		points="30,30 40,200 170,130"
		transform="translate(350, 0) scale(-1, 1)"
		/>"""
	print """<polygon
		style="fill:#e9afaf;fill-opacity:1;stroke:none;stroke-width:4;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
		points="45,60 50,200 150,130"
		transform="translate(350, 0) scale(-1, 1)"
		/>"""

def head():
	# cabeza
	print """<ellipse
		 style="fill:""" + base_color + """;fill-opacity:1;stroke:none;stroke-width:4;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
		 ry="124"
		 rx="146"
		 cy="220"
		 cx="175" />"""

def eyes():
	#ojos
	if selectedeye == 1:
		# ojo izquierdo
		print """<path
	     style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:3.15166402;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="m -0.02004253,29.377348 c 16.41440053,-40.7354 71.10771053,-37.6849605 85.48671053,0.7159 -20.30771,37.343 -72.02061,33.6742 -85.48671053,-0.7159 z"
	     id="path4273"
		 transform="translate(55, 180)"
		 />
	  <path
	     style="fill:""" + eye_color + """;fill-opacity:1;stroke:none;stroke-width:4;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="m 58.307058,28.043288 a 13.763329,26.390236 0 0 1 -13.7634,26.39026 13.763329,26.390236 0 0 1 -13.7633,-26.39026 13.763329,26.390236 0 0 1 13.7633,-26.3902405 13.763329,26.390236 0 0 1 13.7634,26.3902405 z"
		 transform="translate(55, 180)"
		 />"""

		# ojo derecho
		print """<path
	     style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:3.15166402;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="m -0.02004253,29.377348 c 16.41440053,-40.7354 71.10771053,-37.6849605 85.48671053,0.7159 -20.30771,37.343 -72.02061,33.6742 -85.48671053,-0.7159 z"
	     id="path4273"
		 transform="translate(210, 180)"
		 />
	  <path
	     style="fill:""" + eye_color + 	  """;fill-opacity:1;stroke:none;stroke-width:4;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="m 58.307058,28.043288 a 13.763329,26.390236 0 0 1 -13.7634,26.39026 13.763329,26.390236 0 0 1 -13.7633,-26.39026 13.763329,26.390236 0 0 1 13.7633,-26.3902405 13.763329,26.390236 0 0 1 13.7634,26.3902405 z"
		 transform="translate(210, 180)"
		 />"""
	elif selectedeye == 2:
		#ojo izquierdo
		print """<path
	     style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:6;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="M 49.665811,4.200891 C -4.9103195,-3.994289 1.3093705,42.004791 5.8658405,44.307591"
	     transform="translate(65, 180)"/>
	  <ellipse
	     style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:3;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     id="path4165"
	     cx="42.126831"
	     cy="26.837549"
	     rx="27.400574"
	     ry="26.837549"
		 transform="translate(65, 180)"/>"""
		#ojo derecho
 		print """<path
 	     style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:6;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
 	     d="M 49.665811,4.200891 C -4.9103195,-3.994289 1.3093705,42.004791 5.8658405,44.307591"
 	     transform="translate(210, 180)"/>
 	  <ellipse
 	     style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:3;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
 	     id="path4165"
 	     cx="42.126831"
 	     cy="26.837549"
 	     rx="27.400574"
 	     ry="26.837549"
 		 transform="translate(210, 180)"/>"""
	elif selectedeye == 3:
		# ojo izquierdo
		print """
		<path
	     style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="M 77.322166,0.64160424 A 38.661083,26.649874 0 0 1 57.722287,23.827272 38.661083,26.649874 0 0 1 18.795618,23.504219 38.661083,26.649874 0 0 1 0.01120601,0"
		 transform="translate(65, 200)"/>
	  <path
	     style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="M 53.185778,0.63057614 A 14.423838,21.90185 0 0 1 46.372179,21.468153 14.423838,21.90185 0 0 1 31.05156,21.238228 14.423838,21.90185 0 0 1 24.510526,0.20023031"
		 transform="translate(65, 200)"/>"""
		# ojo derecho
		print """
		<path
	     style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="M 77.322166,0.64160424 A 38.661083,26.649874 0 0 1 57.722287,23.827272 38.661083,26.649874 0 0 1 18.795618,23.504219 38.661083,26.649874 0 0 1 0.01120601,0"
		 transform="translate(205, 200)"/>
	  <path
	     style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="M 53.185778,0.63057614 A 14.423838,21.90185 0 0 1 46.372179,21.468153 14.423838,21.90185 0 0 1 31.05156,21.238228 14.423838,21.90185 0 0 1 24.510526,0.20023031"
		 transform="translate(205, 200)"/>
		"""
	elif selectedeye == 4:
		# ojo izquierdo
		print """<ellipse
	     style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     id="path5353"
	     cx="18.392166"
	     cy="18.153307"
	     rx="18.392166"
	     ry="18.153307"
		 transform="translate(90, 190)" />"""
		# ojo derecho
		print """<ellipse
	     style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     id="path5353"
	     cx="18.392166"
	     cy="18.153307"
	     rx="18.392166"
	     ry="18.153307"
		 transform="translate(220, 190)" />"""
	elif selectedeye == 5:
		# ojo izquierdo
		print """<ellipse
	     style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     cx="22.333345"
	     cy="33.593853"
	     rx="22.333345"
	     ry="33.593853"
		 transform="translate(85, 165)"/>
	  <path
	     style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="m 29.706395,38.537881 c 0,13.3371 -6.28657,21.3982 -14.48517,21.3982 -8.1985996,0 -14.84487661,-10.8118 -14.84487561,-24.149 -1e-6,-13.3371 6.64627601,-24.149 14.84487561,-24.149 7.42485,0 13.41669,5.7237 14.5117,17.3037 0.0781,0.8256 -12.77865,6.1623 -12.75336,7.0133 3.97059,1.1298 8.87547,1.6422 12.72683,2.5828 z"
	     transform="translate(85, 165)" />"""
		# ojo derecho
		print """<ellipse
	     style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     cx="22.333345"
	     cy="33.593853"
	     rx="22.333345"
	     ry="33.593853"
		 transform="translate(220, 165)"/>
	  <path
	     style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="m 29.706395,38.537881 c 0,13.3371 -6.28657,21.3982 -14.48517,21.3982 -8.1985996,0 -14.84487661,-10.8118 -14.84487561,-24.149 -1e-6,-13.3371 6.64627601,-24.149 14.84487561,-24.149 7.42485,0 13.41669,5.7237 14.5117,17.3037 0.0781,0.8256 -12.77865,6.1623 -12.75336,7.0133 3.97059,1.1298 8.87547,1.6422 12.72683,2.5828 z"
	     transform="translate(220, 165)" />"""
	elif selectedeye == 6:
		# ojo izquierdo
		print """<path
	     style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:12;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="M 0,6 76.57147,6"
		 transform="translate(65, 200)"/>"""
		# ojo derecho
		print """<path
	     style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:12;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     d="M 0,6 76.57147,6"
		 transform="translate(200, 200)"/>"""
	elif selectedeye == 7:
		# ojo izquierdo
		print """<circle
	     style="fill:""" + eye_color + """;fill-opacity:1;stroke:none;stroke-width:12;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     id="path7220"
	     cx="35.282932"
	     cy="35.282932"
	     r="35.282932"
		 transform="translate(65, 165)"/>
	  <ellipse
	     style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:12;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     id="path7222"
	     cx="35.658283"
	     cy="37.159641"
	     rx="22.89637"
	     ry="22.14567"
		 transform="translate(65, 165)"/>"""
		# ojo derecho
		print """<circle
	     style="fill:""" + eye_color + """;fill-opacity:1;stroke:none;stroke-width:12;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     id="path7220"
	     cx="35.282932"
	     cy="35.282932"
	     r="35.282932"
		 transform="translate(205, 165)"/>
	  <ellipse
	     style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:12;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     id="path7222"
	     cx="35.658283"
	     cy="37.159641"
	     rx="22.89637"
	     ry="22.14567"
		 transform="translate(205, 165)"/>"""



def snout():
	# bocico
	if hassnout:
		print """<ellipse
	     style="fill:""" + snout_color + """;fill-opacity:1;stroke:none;stroke-width:3;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	     cx="71.316559"
	     cy="47.669491"
	     rx="71.316559"
	     ry="47.669491"
		 transform="translate(102, 230)"/>"""

def mouth():
	# boca
	print """<path
     style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:4;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
     d="m 57.127226,0.73613 c 0,60.0225 -54.0044696,36.0135 -55.1295796,12.8048 M 57.183486,0 c 0,60.02253 54.004464,36.01353 55.129574,12.8048"
	 transform="translate(116, 260)"
	 />"""

def nose():
	# nariz
	print """<path
     style="fill:#e9afaf;fill-opacity:1;stroke:none;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
     d="M 37.749457,10.978806 C 37.749467,5.5855058 32.80954,0.30020579 25.45282,0.00700579 c -4.36792,-0.1741 -4.30557,2.95430001 -6.57809,2.95430001 -2.35062,0 -2.24786,-3.36100001 -6.56845,-2.91010001 C 5.01759,0.81200579 0,5.6372058 0,10.978806 c 11.34021,20.1834 28.18045,19.8933 37.749457,0"
     transform="translate(155, 240)"
	 />"""

def lines():
	if haslines:
		#lineas1
		print """
		<path
	     style="fill:""" + stripes_color + """;fill-opacity:1;fill-rule:evenodd;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
	     d="m 6.8695983,3.8070953 c -9.38376,46.9187897 -9.17344,70.1013497 0.75069,64.3725697 C 18.023978,62.174055 21.548988,2.0241753 20.241448,2.0241753 19.147388,0.89052534 6.7746983,2.5900053 6.8695983,3.8070953 Z"
	     transform="translate(142, 94)"/>
	  <path
	     style="fill:""" + stripes_color + """;fill-opacity:1;fill-rule:evenodd;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
	     d="m 59.446868,2.8482053 c 9.383756,46.9187997 9.173436,70.1013597 -0.75069,64.3725797 -10.40369,-6.00561 -13.9287,-66.1554897 -12.62116,-66.1554897 1.09406,-1.13364996 13.46675,0.56583 13.37185,1.78291 z"
	     transform="translate(142, 95)"/>
	  <path
	     style="fill:""" + stripes_color + """;fill-opacity:1;fill-rule:evenodd;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
	     d="m 27.465118,1.1363653 c -9.38376,46.9187997 -0.98013,82.0676997 8.944,76.3389197 10.40369,-6.00561 5.60269,-76.79476966 4.29515,-76.79476966 -1.09406,-1.13365 -13.33405,-0.76123 -13.23915,0.45584996 z"
	     transform="translate(142, 95)"/>"""

		# lineas2
		#izquierda
		print """<path
	     style="fill:""" + stripes_color + """;fill-rule:evenodd;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
	     d="M 0,17.445334 C 37.68862,0.98973446 47.11077,-6.4418655 42.33334,6.8288345 37.55591,20.099434 6.76803,28.592634 6.76803,28.592634 4.1657,24.942434 0.85644,21.270134 0,17.445334 Z"
		 transform="translate(43, 255)"	 />
	  <path
	     style="fill:""" + stripes_color + """;fill-rule:evenodd;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
	     d="m 11.80172,33.883434 c 28.17178,-14.1874 35.21472,-20.5946 31.64365,-9.1532 -3.57107,11.4415 -24.05102,17.8256 -24.05102,17.8256 -1.94522,-3.147 -6.95246,-5.3749 -7.59263,-8.6724 z"
		 transform="translate(42, 255)"/>"""
		# derecha
		print """<path
	     style="fill:""" + stripes_color + """;fill-rule:evenodd;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
	     d="M 0,17.445334 C 37.68862,0.98973446 47.11077,-6.4418655 42.33334,6.8288345 37.55591,20.099434 6.76803,28.592634 6.76803,28.592634 4.1657,24.942434 0.85644,21.270134 0,17.445334 Z"
		 transform="translate(308, 255) scale(-1, 1)"	 />
	  <path
	     style="fill:""" + stripes_color + """;fill-rule:evenodd;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
	     d="m 11.80172,33.883434 c 28.17178,-14.1874 35.21472,-20.5946 31.64365,-9.1532 -3.57107,11.4415 -24.05102,17.8256 -24.05102,17.8256 -1.94522,-3.147 -6.95246,-5.3749 -7.59263,-8.6724 z"
		 transform="translate(308, 255) scale(-1, 1)"/>"""

def whiskers():
	# bigotes
	if haswhiskers:
		print """
		 <path
	    style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	    d="M 0.76440037,15.283171 84.104009,14.752341 4.4801804,26.961331 M 83.573179,14.619631 0.23358037,1.4817013"
		transform="translate(0, 235)"
	    />"""
		print """
		 <path
	    style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
	    d="M 0.76440037,15.283171 84.104009,14.752341 4.4801804,26.961331 M 83.573179,14.619631 0.23358037,1.4817013"
		transform="translate(353, 235) scale(-1, 1)"
	    />"""

def endgroup():
	# cerramos el grupo
	print """
</g>"""

def footer():
	#cerramos el tag <svg>
	print """
</svg>"""


def setparams():
	global selectedeye
	global base_color
	global eye_color
	global stripes_color
	global snout_color
	global ears_color
	global hassnout
	global haswhiskers
	global haslines

	hue = random.random()
	basergb = hsv2rgb(hue, 0.24, 1.0)
	eyergb = hsv2rgb(1-hue, 0.67, 1.0)
	stripesrgb = hsv2rgb(hue, 0.24, 0.8)

	if (random.randint(1, 10) > 9):
		basergb = (255, 255, 255)
		stripesrgb = (236, 236, 236)
	if (random.randint(1, 10) > 9):
		basergb = (106, 106, 106)
		stripesrgb = (76, 76, 76)

	base_color = '#%02x%02x%02x' % basergb
	eye_color = '#%02x%02x%02x' % eyergb
	stripes_color = '#%02x%02x%02x' % stripesrgb
	snout_color = '#%02x%02x%02x' % random.choice([(255, 255, 255), (255, 255, 255), (106, 106, 106)])
	ears_color = random.choice(["#ffffff", base_color, stripes_color, "#6a6a6a"])

	hassnout = 	True
	haswhiskers = True
	haslines = False

	if (random.randint(1, 3) > 2):
		hassnout = False
	if (random.randint(1, 4) > 3):
		haswhiskers = False
	if (random.randint(1, 4) > 3):
		haslines = True

	selectedeye = random.randint(1, 7)

def drawcat(x, y, scale):
	setparams()
	group(x, y, scale)
	ears()
	head()
	eyes()
	snout()
	mouth()
	nose()
	lines()
	whiskers()
	endgroup()

def main(argv):
	number = 1
	scale = 0.25
	header(number, scale*10)
	for i in range(0, number):
		drawcat((i % columns) * 400, (i/columns) * 350, scale)
	footer()

if __name__ == "__main__":
	main(sys.argv[1:])
