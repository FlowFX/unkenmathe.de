<?php snippet('header') ?>



<?php if($error): ?>
	<div class="alert"><?php echo $page->alert()->html() ?></div>
<?php endif ?>

	<form method="post" class="form-inline">
		<div class="form-group">
			<label for="username"><?php echo $page->username()->html() ?></label>
			<input type="text" id="username" name="username">
		</div>
		<div class="form-group">
			<label for="password"><?php echo $page->password()->html() ?></label>
			<input type="password" id="password" name="password">
		</div>
		<div class="form-group">
			<input type="submit" class="btn btn-default" name="login" value="<?php echo $page->button()->html() ?>">
		</div>
	</form>



<?php snippet('footer') ?>
