<nav class="navbar navbar-default" role="navigation">
	<div class="container">
		<div class="navbar-header">
			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
				<span class="sr-only">Toggle navigation</span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			<a class="navbar-brand" href="<?php echo $site->url() ?>">
				<img class="img-responsive" alt="Logo" src="<?php echo $site->image('frog-logo.png')->url() ?>">
			</a>
		</div>
		<div id="navbar" class="collapse navbar-collapse">

			<?php $items = $pages->visible(); ?>
			<ul class="nav navbar-nav">

				<?php foreach($items as $item): ?>
					<li<?php e($item->isOpen(), ' class="active"') ?> role="presentation"><a href="<?php echo $item->url() ?>"><?php echo $item->title()->html() ?></a></li>
				<?php endforeach ?>

			</ul>



			<ul class="nav navbar-nav navbar-right">
				<?php if($user = $site->user()): ?>
					<li class="dropdown">
						<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">Hallo <?php echo $user->username() ?> <span class="caret"></span></a>
						<ul class="dropdown-menu" role="menu">
							<li><a href="<?php echo $site->url() . "/panel/#/" ?>">Panel</a></li>
							<li><a href="<?php echo $pages->find('redaktion')->url() ?>">Redaktion</a></li>
							<li class="divider"></li>
							<li><a href="<?php echo $site->url() . "/panel/#/users/edit/" . $user->username() ?>">Profil</a></li>
							<li><a href="<?php echo url('logout') ?>">Abmelden</a><li>
						</ul>
				<?php else : ?>
					<li><a href="<?php echo url('login') ?>" title="Anmelden">Anmelden</a></li>
				<?php endif ?>
			</ul>
		</div><!--/.navbar-collapse -->
	</div>
</nav>
