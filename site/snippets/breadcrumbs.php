

<ol class="breadcrumb">
	<li>
		<a href="<?php echo $site->url() ?>">Start</a>
	</li>
	<li>
		<a href="<?php echo $page->parent()->url() ?>"><?php echo html($page->parent()->title()) ?></a>
	</li>
	<li>
		<?php echo html($page->title()) ?>
	</li>
</ol>