<?php snippet('header') ?>



<?php if( $user_is_editor ): ?>
	<p><a href="<?php echo url('panel/#/pages/add/' . $page->uri()) ?>">Neue Aufgabe erstellen</a></p>
<?php endif ?>

	<div id="filters">
		<h4>Thema</h4>
		<div data-filter-group="tags" class="btn-group btn-group-sm">
			<button data-filter="" type="button" class="btn btn-success active um-keyword">Alle</button>
			<?php foreach($all_tags as $tag): ?>
				<button data-filter="<?php echo '.'.tagslug($tag) ?>" type="button" class="btn btn-primary um-keyword"><?php echo html($tag) ?></button>
			<?php endforeach ?>
		</div>
		<h4>Klassenstufe</h4>
		<div data-filter-group="class" class="btn-group btn-group-sm">
			<button data-filter="" type="button" class="btn btn-danger um-keyword active">Alle</button>
			<?php foreach($all_levels as $level): ?>
				<button data-filter="<?php echo '.' . $level ?>" type="button" class="btn btn-primary um-keyword"><?php echo $level ?></button>
			<?php endforeach ?>
		</div>
	</div>

	<div id="container">
		<?php foreach($items as $item): ?>

			<!-- add every keyword as class -->
			<div class="item col-sm-6 col-md-4 col-lg-3<?php echo ' '.$item->level() ?><?php foreach($item->tags()->split(',') as $single_tag): echo ' '.tagslug($single_tag); endforeach ?>">


				<h3><a href="<?php echo $item->url() ?>"><?php echo $item->title()->html() ?></a></h3>

				<p>Lizenz: <?php echo $item->license()->html() ?></p>
				<p>Quelle: <a href="<?php echo $item->link() ?>"><?php echo $item->source()->html() ?></a></p>
				<p>Schlagworte: <?php echo $item->tags()->html() ?></a></p>

				<!-- frontend tests of content items -->
				<?php if( $user_is_editor ): ?>
					<?php if( !$item->license()->split(',') ) : ?>
						<div class="alert alert-danger" role="alert">Keine Lizenz</div>
					<?php endif ?>
					<?php if( !$item->level()->split(',') ) : ?>
						<div class="alert alert-warning" role="alert">Keine Klassenstufe</div>
					<?php endif ?>
					<?php if( !$item->tags()->split(',') ) : ?>
						<div class="alert alert-info" role="alert">Keine Schlagworte</div>
					<?php endif ?>
				<?php endif ?>


				<!-- print the item's fist html file -->
				<?php echo $item->files()->filterby('extension', 'html')->first()->read() ?>

			</div>
		<?php endforeach ?>
	</div>




<?php snippet('footer') ?>