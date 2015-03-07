<?php
	// only show this site to logged in users
	// todo: only show it to admins and editors
	if(!$site->user()) go('/')
?>

<?php snippet('header') ?>

<?php echo $page->text()->kirbytext() ?>



<div class="table-responsive um-redaktion">
<table class="table table-condensed table-striped">
	<thead>
		<tr>
			<th>Slug</th>
			<th>Titel</th>
			<th>Vorschau</th>
			<th>Public</th>
			<th>Themengebiet</th>
			<th>Klasse</th>
			<th>Thema</th>
			<th>HTML</th>
			<th>LaTeX</th>
			<th>DOCX</th>
			<th>Quelle</th>
			<th>Autor</th>
			<th>Lizenz</th>
			<th>Link</th>
			<th>Edit</th>
		</tr>
	</thead>
	<tbody>
		<?php foreach($site->children()->children() as $item): ?>
			<tr>
				<!-- Slug, Title, Visibility -->
				<td><a href="<?php echo url($item) ?>"><?php echo html($item->slug()) ?></a></td>
				<td><?php echo html($item->title()) ?></td>
				<td><!-- Button trigger modal --><button type="button" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#myModal-<?php echo $item->hash() ?>">Vorschau</button>

<!-- Modal -->
<div class="modal fade" id="myModal-<?php echo $item->hash() ?>" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
				<h4 class="modal-title" id="myModalLabel"><?php echo $item->title()->html() ?></h4>
      </div>
      <div class="modal-body">
				<?php echo $item->text()->kirbytext() ?>
      </div>
    </div>
  </div>
</div>
</td>

				<td class="text-center"><?php e( $item->isVisible(), '<span class="glyphicon glyphicon-ok"') ?></td>

				<!-- Topic, Level, Tags -->
				<td><?php echo html($item->parent()->title()) ?></td>
				<td><?php echo html($item->level()) ?></td>
				<td><?php echo html($item->tags()) ?></td>

				<!-- Files -->
				<td class="text-center"><?php e( $item->files()->filterby('extension', 'tex')->first(), '<span class="glyphicon glyphicon-ok"></span>', '<span class="glyphicon glyphicon-remove"></span>' ) ?></td>
				<td class="text-center"><?php e( $item->files()->filterby('extension', 'html')->first(), '<span class="glyphicon glyphicon-ok"></span>', '<span class="glyphicon glyphicon-remove"></span>' ) ?></td>
				<td class="text-center"><?php e( $item->files()->filterby('extension', 'docx')->first(), '<span class="glyphicon glyphicon-ok"></span>', '<span class="glyphicon glyphicon-remove"></span>' ) ?></td>

				<!-- Source, Author, License, Link -->
				<td><?php echo html($item->source()) ?></td>
				<td><?php echo html($item->author()) ?></td>
				<td><?php echo link_to_license($item->license()) ?></td>
				<td class="text-center"><?php if($item->link()->split(',')): ?><a href="<?php echo $item->link() ?>"><span class="glyphicon glyphicon-link" aria-hidden="true"></span></a><?php endif ?></td>
				<td class="text-center"><a href="<?php echo url('panel/#/pages/show/' . $item->uri()) ?>"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span></a></td>

			</tr>
		<?php endforeach ?>
	</tbody>
</table>
</div>


<?php snippet('footer') ?>
