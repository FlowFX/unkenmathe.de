<?php snippet('header') ?>

<?php snippet('breadcrumbs') ?>


<?php if( $user_is_editor ): ?>
		<p><a href="<?php echo $link_edit ?>" title="Aufgabe bearbeiten">Bearbeiten</a></p>
<?php endif ?>



<div class="container um-item">

	<div class="row">

		<div class="col-md-10 um-item-text">
			<?php echo $page->text()->kirbytext() ?>
		</div>


		<?php if( $site->user() ): // show download links only for logged in users, i.e. 'lehrer' ?>
		<div class="col-md-2">
			<p>
				<a href="<?php echo $file_latex->url() ?>" title="LaTeX-Quellcode herunterladen"><button type="button" class="btn btn-default"><span class="glyphicon glyphicon-cloud-download"></span> \( \LaTeX \)</button></a>
				<a href="<?php echo $file_docx->url() ?>" title="docx-Dokument herunterladen"><button type="button" class="btn btn-default"><span class="glyphicon glyphicon-cloud-download"></span> docx</button></a>
			</p>
		</div>
		<div class="col-xs-12 panel panel-default ">
			<div class="panel-heading">
				<p class="panel-title">
					<a data-toggle="collapse" data-target="#collapseSource">
						<span class="glyphicon glyphicon-eye-open"></span> \( \LaTeX \)-Quellcode anzeigen
					</a>
				</p>
			</div>
			<div id="collapseSource" class="panel-collapse collapse">
				<div class="panel-body">
					<pre><code class="tex"><?php echo $file_latex->read() ?></code></pre>
				</div>
			</div>
		</div>
		<?php endif ?>
		<div class="col-md-4">
			<p>Quelle: <?php echo $page->source()->html() ?>; Lizenz: <?php echo link_to_license($page->license()) ?></p>
		</div>


	</div>



<?php snippet('footer') ?>


