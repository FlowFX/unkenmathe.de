<?php

return function($site, $pages, $page) {

	// check if user has editing rights
	if( $user = $site->user() and ( $user->hasRole('editor') or $user->hasRole('admin') ) ):
		$user_is_editor = True;
	else:
		$user_is_editor = False;
	endif;



	// get all items
	$items = $page->children()->visible()->flip();

	// fetch all tags and levels
	$all_tags = $items->pluck('tags', ',', true);
	$all_levels = $items->pluck('level', ',', true);
	$all_licenses = $items->pluck('license', ',', true);

	// pass $items, $all_tags and $all_levels to the template
	return compact('items', 'all_tags', 'all_levels', 'all_licenses', 'user_is_editor');

};