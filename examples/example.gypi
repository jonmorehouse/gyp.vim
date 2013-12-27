{
	# Unit test target
	# Uses kiwi for unit test running
	# Need to create an external script for running the script after and place it in postbuilds...
	"variables" : {

		"name": "unit",
		"plist": "unit/Info.plist",
		"pch": "unit/unit.pch",

	},

	# now include the template
	"includes": ["template.gypi"],
	
	# overwrite the sources directory for now ...
	"sources": [

		"<!@(find unit -type f)",
		"<(plist)",
		"<(pch)",
	],

	# exlucde app sources durin temporary testing
	"sources!": [

		"<@(app_sources)"

	],


	"include_dirs": [

		"unit"
	],

	"postbuilds" : [
			
			{
				"postbuild_name": "run-kiwi-specs",
				"action": ["/bin/bash", "<(scripts_dir)/run_kiwi_specs.sh"]
			}
		]
}
