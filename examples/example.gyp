{

	#############################################################################
	############################# VARIABLES #########################################
	#############################################################################
	"variables" : {

		# initialize product name -- targets are based off of this
		"product_name": "app",
		
		# root directory for all elements
		"root_dir": "<!(pwd)",
		
		# where the code lives!
		"src_dir": "src/code",
		
		# scripts location
		"scripts_dir": "<!(pwd)/scripts",

		# config location
		"config_dir": "config",

		# build location
		"build_dir": "<!(pwd)/build",

		# playlist location with elements
		"plist_file": "src/Info.plist",
		
		# pch file for gcc
		"pch_file": "src/code/app.pch",
	},

	#############################################################################
	############################# XCODE GLOBAL SETTINGS #########################################
	#############################################################################
	"xcode_settings": {
		
		# global sdk / xcode configuration settings
		"SUPPORTED_PLATFORMS" : "iphonesimulator iphoneos",
		"SDKROOT": "iphoneos",

	}, # GLOBAL / DEFAULT Xcode sttings

	# set up mac config 
	"xcode_config_file": "config/shared.xcconfig",

	#############################################################################
	################################## TARGET DEFAULTS ##################################
	#############################################################################
	# global conditions for application
	"target_defaults" : {

		# initialize type of application 
		"type": "executable",
		"mac_bundle": 1,

		# include directories for headers
		"include_dirs": [
			
			"$(inherited)",
			"<(src_dir)",
			"<(src_dir)/BroadcastPlayer",
			"<(src_dir)/Categories",
			"<(src_dir)/Controllers",
			"<(src_dir)/Models",
			"<(src_dir)/Network",
			"<(src_dir)/Support",
			"<(src_dir)/test",
			"<(src_dir)/Tutorial",
			"<(src_dir)/Views",
		],

		# now go ahead and grab all of the correct source files for this application and insert them here
		"sources": [
			"<!@(find <(src_dir) -type f \( -name \"*.m\" -o -name \"*.h\" -o -name \"*.xib\" -o -name \"*.plist\" \))",
			#"<!@(find src/temp_code -type f)",
			"<(plist_file)",
			"<(pch_file)",
		],

		"xcode_settings": {

			"INFOPLIST_FILE": "<(plist_file)",
			"CODE_SIGN_IDENTITY": "iPhone Developer: Sean McCoy (VB4U59V8X7)",
			"CODE_SIGN_IDENTITY[sdk=iphoneos*]" : "iPhone Developer: Sean McCoy (VB4U59V8X7)",
			"PRODUCT_NAME": "app",
			"PROVISIONING_PROFILE": "",
			"PROVISIONING_PROFILE[sdk=iphoneos*]": "",
			"GCC_PREFIX_HEADER": "<(pch_file)",
			"LIBRARY_SEARCH_PATHS": "$(inherited)",
		},

		"link_settings": {

			"libraries": [

				# initialize system frameworks needed
				"$(SDKROOT)/System/Library/Frameworks/OpenGLES.framework",
				"$(SDKROOT)/System/Library/Frameworks/CoreVideo.framework",
				"$(SDKROOT)/System/Library/Frameworks/CoreAudio.framework",
				"$(SDKROOT)/System/Library/Frameworks/AudioToolbox.framework",
				"$(SDKROOT)/System/Library/Frameworks/CoreMedia.framework",
				"$(SDKROOT)/System/Library/Frameworks/CoreTelephony.framework",
				"$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework",
				"$(SDKROOT)/System/Library/Frameworks/Foundation.framework",
				"$(SDKROOT)/System/Library/Frameworks/UIKit.framework",
				"$(SDKROOT)/System/Library/Frameworks/CoreFoundation.framework",
				"$(SDKROOT)/System/Library/Frameworks/MobileCoreServices.framework",
				"$(SDKROOT)/System/Library/Frameworks/Security.framework",
				"$(SDKROOT)/System/Library/Frameworks/AVFoundation.framework",
				"$(SDKROOT)/System/Library/Frameworks/MapKit.framework",
				"$(SDKROOT)/System/Library/Frameworks/CoreLocation.framework",
				"$(SDKROOT)/System/Library/Frameworks/ImageIO.framework",
				"$(SDKROOT)/System/Library/Frameworks/Accounts.framework",
				"$(SDKROOT)/System/Library/Frameworks/AdSupport.framework",
				"$(SDKROOT)/System/Library/Frameworks/CoreText.framework",
				"$(SDKROOT)/System/Library/Frameworks/MessageUI.framework",
				"$(SDKROOT)/System/Library/Frameworks/SystemConfiguration.framework",
				"$(SDKROOT)/System/Library/Frameworks/MediaPlayer.framework",
				"$(SDKROOT)/System/Library/Frameworks/Twitter.framework",
				"$(SDKROOT)/System/Library/Frameworks/Social.framework",
				"$(SDKROOT)/System/Library/Frameworks/CoreData.framework",
				"$(SDKROOT)/System/Library/Frameworks/CFNetwork.framework",
				"$(SDKROOT)/System/Library/Frameworks/QuartzCore.framework",
				"$(SDKROOT)/System/Library/Frameworks/StoreKit.framework",
				"$(SDKROOT)/System/Library/Frameworks/AssetsLibrary.framework",
				
				# other libraries / dynamic libs / non-framework libs
				"$(SDKROOT)/usr/lib/libstdc++.dylib",
				"$(SDKROOT)/usr/lib/libz.dylib",
				"$(SDKROOT)/usr/lib/libicucore.dylib",
				"$(SDKROOT)/usr/lib/libsqlite3.dylib",
			],
		},


	}, # DEFAULT CONDITIONS ETC


	#############################################################################
	################################## TARGETS ##################################
	#############################################################################
	"targets": [

		# debug is for device testing as well as general development testing
		# this can also be updated to testflight as well
		{
			"target_name": "debug",
      			"product_name": "<(product_name).debug",
      			"xcode_config_file": "config/debug.xcconfig",
			
			"postbuilds": [

				#{
				#	"postbuild_name": "test",
				#	"action": ["/bin/bash", "<(scripts_dir)/test.sh"], 
				#}
			],
		},

		# unit testing (kiwi)
		{
			"target_name": "unit",
			"product_name": "<(product_name).unit",
      			"xcode_config_file": "config/unit.xcconfig",
      			# overwrite any xcode settings as needed
      			"xcode_settings": {

				"INFOPLIST_FILE": "unit/Info.plist",
				"GCC_PREFIX_HEADER": "unit/app.pch",
      			},

			"sources": [
				
				"<!@(find unit -type f)",
			]
		},

		# functional testing (kif)
		{

			"target_name": "functional",
			"product_name": "<(product_name).functional",
			"xcode_config_file": "config/functional.xcconfig",

		},

		# integration tests (frank)
		{
			"target_name": "integration",
			"product_name": "<(product_name).integration",
			"xcode_config_file": "config/integration.xcconfig",
		},

		#release
		{

			"target_name": "release",
			"product_name": "<(product_name).release",
			"xcode_config_file": "config/release.xcconfig",
		},

		 #now create an all target
		{
		
			"target_name": "all",
			"product_name": "app.all",
			"dependencies": [
				
				"debug",
				"unit",
				"functional",
			],
		}

	]# end of all targets
}
