<?php if(!defined('KIRBY')) exit ?>

title: Aufgabe
pages: false
files: true
fields:
	title:
		label: Titel
		type:  text
	source:
		label: Ext. Quelle
		type: tags
		index: template
		width: 1/2
	link:
		label: Ext. Link
		type: url
		width: 1/2
	author:
		label: Author
		type: user
		width: 1/2
	license:
		label: Lizenz
		type:  select
		default: CC-BY
		options:
			CC-BY: CC-BY
			CC-BY-SA: CC-BY-SA
		width: 1/4
	level:
		label: Klassenstufe
		type: radio
		default: none
		options:
			5-6: 5-6
			7-8: 7-8
			9-10: 9-10
			11-12: 11-12
		width: 1/2
		required: false
	tags:
		label: Stichworte
		type: tags
		index: template
	text:
		label: Inhalt
		type: textarea
