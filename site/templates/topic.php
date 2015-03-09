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
			<div class="item um-item-text col-sm-6 col-md-4<?php echo ' '.$item->level() ?><?php foreach($item->tags()->split(',') as $single_tag): echo ' '.tagslug($single_tag); endforeach ?>">


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


				<!-- Item text -->
				<?php echo $item->text()->kirbytext() ?>

				<p><a href="<?php echo $item->url() ?>" title="Zur Aufgabe">Mehr…</a></p>

			</div>
		<?php endforeach ?>
	</div>




<?php snippet('footer') ?>
