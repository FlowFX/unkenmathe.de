<?php

/**
 * Unkenmathe specific functions
 *
 * @author Florian Posdziech <florian@unkenmathe.de>
 * @version 0.0.1
 */


function link_to_license($license)
{

	switch ($license) {
		case "CC-BY":
			$link = '<a href="https://creativecommons.org/licenses/by/4.0/" title="Creative Commons Attribution 4.0 International (CC BY 4.0)" rel="nofollow">CC-BY</a>';
			break;
		case "CC-BY-SA":
			$link = '<a href="https://creativecommons.org/licenses/by-sa/4.0/" title="Creative Commons Attribution 4.0 International (CC BY SA 4.0)" rel="nofollow">CC-BY-SA</a>';
			break;
		default:
			$link = 'n/a';
			break;
	}

	return $link;

}

?>
