<?php

return function($site, $pages, $page) {


	// check if user has editing rights
	if( $user = $site->user() and ( $user->hasRole('editor') or $user->hasRole('admin') ) ):
		$user_is_editor = True;
	else:
		$user_is_editor = False;
	endif;


	// edit link
	$link_edit = url('panel/#/pages/show/' . $page->uri());

	// download links
	$file_html = $page->files()->filterby('extension', 'html')->first();
	$file_latex = $page->files()->filterby('extension', 'tex')->first();
	$file_docx = $page->files()->filterby('extension', 'docx')->first();

	// pass $items, $all_tags and $all_levels to the template
	return compact('link_edit', 'file_html', 'file_latex', 'file_docx', 'link_license', 'link_license_title', 'license', 'user_is_editor');

};


