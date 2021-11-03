#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

cgitb.enable()
import db

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
form=cgi.FieldStorage()
hbdb=db.Pet('localhost','usuario','usuario','foundbypets')

data=(form['nombre'].value,form['region'].value,form['conmuna'].value,form['celular'].value,form['email'].value,form["file"])
hbdb.save_pet2(data)


mensaje="""
<!DOCTYPE html>
<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="fr"> <![endif]-->
<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="fr"> <![endif]-->
<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="fr"> <![endif]-->
<!--[if gt IE 8]> <html class="no-js" lang="fr"> <![endif]-->
<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Prototipo pagina web</title>
		<!--BEGIN OF TERMS OF USE. DO NOT EDIT OR DELETE THESE LINES. IF YOU EDIT OR DELETE THESE LINES AN ALERT MESSAGE MAY APPEAR WHEN TEMPLATE WILL BE ONLINE-->
<style>#free-flash-header a,#free-flash-header a:hover {color:#363636;}#free-flash-header a:hover {text-decoration:none}</style>
<!--END OF TERMS OF USE-->

		<!-- Bootstrap -->
		<link href="../css/reset.css" rel="stylesheet" type="text/css" media="all">
		<link href="../css/bootstrap.css" rel="stylesheet" type="text/css" media="all">
		<link href="../css/style.css" rel="stylesheet" type="text/css" media="all">
		<link href="../css/font.css" rel="stylesheet" type="text/css" media="all">
		<link href="../css/mobile.css" rel="stylesheet" type="text/css" media="all">
		<!-- end Bootstrap -->
		<link href='http://fonts.googleapis.com/css?family=Allura|Great+Vibes|Linden+Hill:400,400italic' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Lato:400,400italic,700,700italic,900,900italic,300italic,300,100italic,100' rel='stylesheet' type='text/css'>

		<!-- LightBox -->
		<link href="../css/lightbox/vlightbox.css" rel="stylesheet" type="text/css" media="all">
		<link href="../css/lightbox/visuallightbox.css" rel="stylesheet" type="text/css" media="all">
		<link rel="stylesheet" type="text/css" href="css/lightbox/style.css" />
		<!-- end LightBox -->

		<!--[if lt IE 9]>
		  <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
		  <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
		<![endif]-->

	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
  	<script src="../js/main.js"></script>

	</head>
	
	<body>
	<div class="global-container">
			<!--BEGIN OF TERMS OF USE. DO NOT EDIT OR DELETE THESE LINES. IF YOU EDIT OR DELETE THESE LINES AN ALERT MESSAGE MAY APPEAR WHEN TEMPLATE WILL BE ONLINE-->
	<div id="copy" style="height: 75px; position: absolute; bottom: 0px; left:0px; border: none; width: 100%;">
		<div id="free-flash-header" style="width:820px;margin:0 auto;text-align:right;position:relative;bottom:0px;margin-top:63px;color:#363636;font-size:10px;font-family:Verdana"><strong>prototipo de pagina</strong> en <a href="http://www.freeplantillas.com/"><strong>descargar musica gratis</strong></a></div>
	</div>	
	<!--END OF TERMS OF USE-->	
		<div class="page-container">
			<header>
				<div class="container no_left no_right">
					<div class="row">

						
						<div class="col-md-4 col-xs-12">
							<!-- logo -->
							<div class="logo">
								<a href="index.htm">
									<img src="images/logo.png" alt="logo">
								</a>

								<p class="slogan">
								</p>
							</div>	
							<!-- logo -->

						</div>	
						
					

						<div class="col-md-8 col-xs-12 right_header no_left no_right">

							<!-- menu -->	
							<nav class="menu" style="margin-bottom:1px;">
								<ul>
									<li>
										<a href="index.htm">
											<span>Comenzar aquí</span>
										</a>
									</li>
									<li>
										<a href="encontrada.htm">
											<span>Macota encontrada</span>
										</a>
									</li>
									<li>
										<a href="perdida.htm">
											<span>Macota perdida</span>
										</a>
									</li>
									<li>
										<a href="contacto.htm">
											<span>Contacto</span>
										</a>
									</li>
									<li>
										<a href="https://www.instagram.com/foundbypets/">
											<span>Instagram</span>
										</a>
									</li>

								</ul>
							</nav>
							<!-- menu -->

							<div class="clear"></div>

							<!-- slide -->
							<div class="slide">
								<div id="wowslider-container1">
									<div class="ws_images"><ul>
											<li><img src="../images/flashimages/header1.jpg" alt="" title="YOUR BEAUTY WEBSITE" id="wows1_0"/>YOUR OWN SLOGANS AND IMAGES</li>
											<li><img src="../images/flashimages/header2.jpg" alt="" title="YOUR BEAUTY WEBSITE" id="wows1_1"/>YOUR OWN SLOGANS AND IMAGES</li>
											<li><img src="../images/flashimages/header3.jpg" alt="" title="YOUR BEAUTY WEBSITE" id="wows1_2"/>YOUR OWN SLOGANS AND IMAGES</li>
											<li><img src="../images/flashimages/header1.jpg" alt="" title="YOUR BEAUTY WEBSITE" id="wows1_2"/>YOUR OWN SLOGANS AND IMAGES</li>
										</ul>
									</div>
								</div>
							</div>
							<!-- slide -->
						</div>

					</div>
				</div>
			</header>

		<div style="padding:0 16px;">
    <h1>El formulario se ha enviado con exito</h1>

		<!-- footer -->
		<footer class="footer container">
			<nav class="footer">
				<ul>
					<li>
						<a href="../index.html">About us</a>
					</li>
					<li>
						<a href="../index.html">Locations</a>
					</li>
					<li>
						<a href="../contacto.html">Contact</a>
					</li>
					<li>
						<a href="../index.html">Jobs</a>
					</li>
					<li>
						<a href="../index.html">Press</a>
					</li>
				</ul>
			</nav>
			<div class="container copyright">
				<p>© Copyright 2015 Company. All right reserved </p>
			</div>
		</footer>
		<!-- end footer -->

	<audio id="audio-bg">
	    <!--source src="audio/music.mp3"-->
	</audio>

    <script type='text/javascript' src="../js/jquery-2.1.3.js"></script>
    <script type='text/javascript' src="../assets/js/visuallightbox.js"></script>
    <script type='text/javascript' src="../assets/js/vlbdata.js"></script>
    <script type="text/javascript" src="../assets/js/wowslider.js"></script>
    <script type="text/javascript" src="../assets/js/wowslider-gallery.js"></script>
	<script type="text/javascript" src="../assets/js/script.js"></script>
	<script type="text/javascript" src="../assets/js/script-gallery.js"></script>
    <script type='text/javascript' src="../js/app.js"></script>

   </div>
  </body>
</html>
        """
print(mensaje)