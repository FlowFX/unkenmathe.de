<?php

/*

---------------------------------------
License Setup
---------------------------------------

Please add your license key, which you've received
via email after purchasing Kirby on http://getkirby.com/buy

It is not permitted to run a public website without a
valid license key. Please read the End User License Agreement
for more information: http://getkirby.com/license

*/

c::set('license', 'K2-PERSONAL-2469c3172dc74f116c9cb6451127b49a');

/*

---------------------------------------
Kirby Configuration
---------------------------------------

By default you don't have to configure anything to
make Kirby work. For more fine-grained configuration
of the system, please check out http://getkirby.com/docs/advanced/options

*/


c::set('locale', 'de_DE.UTF8');

// Enable Markdown Extra
// cf. http://getkirby.com/docs/content/text#markdown-extra
c::set('markdown.extra', true);

// Suppress markdown linebreaks
c::set('markdown.breaks', false);


// User roles
c::set('roles', array(
	array(
		'id'      => 'admin',
		'name'    => 'Admin',
		'panel'   => true
	),
	array(
		'id'      => 'editor',
		'name'    => 'Redakteur',
		'panel'   => true
	),
	array(
		'id'      => 'guest',
		'name'    => 'Gast',
		'panel'   => false,
		'default' => true
	)
));



// The logout
// For the logout we don't need a real page. A simple URL to send logged in users to is enough.
// This is a perfect example for Kirby's new router.

c::set('routes', array(
	array(
		'pattern' => 'logout',
		'action'  => function() {
			if($user = site()->user()) $user->logout();
			go('login');
		}
	)
));
