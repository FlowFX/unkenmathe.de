<?php snippet('header') ?>



<?php if($error): ?>
	<div class="alert"><?php echo $page->alert()->html() ?></div>
<?php endif ?>

	<form method="post">
		<div>
			<label for="username"><?php echo $page->username()->html() ?></label>
			<input type="text" id="username" name="username">
		</div>
		<div>
			<label for="password"><?php echo $page->password()->html() ?></label>
			<input type="password" id="password" name="password">
		</div>
		<div>
			<input type="submit" name="login" value="<?php echo $page->button()->html() ?>">
		</div>
	</form>




<?php snippet('footer') ?>
