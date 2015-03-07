<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title><?php echo $site->title()->html() ?> | <?php echo $page->title()->html() ?></title>
	<meta name="description" content="<?php echo $site->description() ?>">

	<?php echo css('assets/css/style.css') ?>

	<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
	<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
	<!--[if lt IE 9]>
	<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
	<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	<![endif]-->


	<script type="text/x-mathjax-config">
		MathJax.Hub.Config({
  			extensions: ['tex2jax.js'],
  			jax: ['input/TeX','output/HTML-CSS'],
  			tex2jax: {
    			inlineMath: [ ['$','$'], ['\\(','\\)'] ],
    			processEscapes: true
  			}
		});
	</script>

</head>
<body>
<div id="wrap">
	<main>

		<?php snippet('navbar') ?>

		<div class="container">

			<div class="page-header">
				<h1><?php echo $page->title()->html() ?></h1><small><?php echo $page->intro()->kirbytext() ?></small>
			</div>

