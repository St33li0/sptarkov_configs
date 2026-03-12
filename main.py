# Main.py
# Modpack Manager Entry Point

import os
import sys

import argparse

parser = argparse.ArgumentParser(
					prog = 'SPT_CBMM',
					description = 'Config Based Modpack Manager for SinglePlayer Tarkov',
					epilog = 'Are you ready to die?')
parser.suggest_on_error = True
parser.add_argument("-i","--sptdir",default="C:\\SPT",help="Directory of SPT Installation. Defaults to C:\\SPT")
parser.add_argument("-s","--stagingdir",default="C:\\SPT\\SPT_CBMM_Staging",help="Directory to stage mods and store backups. Default = '$SPTDIR\\SPT_CBMM_Staging'")
parser.add_argument("-u","--url",default="https://github.com/St33li0/sptarkov_configs",help="Best not to change this unless you know what you are doing.")
parser.add_argument("-f","--force",default=False,action="store_true",help="Does not prompt user for confirmation when enabled.")

# def get_arg_dict(args):
# 	return {
# 		spt_install_dir: args.sptdir,
# 		mod_staging_dir: args.stagingdir,
# 		modpack_source_url: args.url
# 	}

# args = get_arg_dict(parser.parse_args())

parsed = parser.parse_args()

if parsed.sptdir != "C:\\SPT" and parsed.stagingdir == "C:\\SPT\\SPT_CBMM_Staging":
	parsed.stagingdir = (f"{parsed.sptdir}\\SPT_CBMM_Staging")

args = {
	"spt_install_dir": parsed.sptdir,
	"mod_staging_dir": parsed.stagingdir,
	"modpack_source_url": parsed.url
}

if not parsed.force:
	print(f"""The program is running with the following variables:
			SPT Install Directory :: {args["spt_install_dir"]}
			Mod Staging Directory :: {args["mod_staging_dir"]}
			  Modpack Source URL  :: {args["modpack_source_url"]}
			""")
	print("Are the above variables set correctly? [Y/n]")
	i = input()
	if i.lower() != "y":
		parser.print_help()
		sys.exit(0)

SPT_MODS_FOLDER = {
	"BepInEx": {"root":(f"{args["spt_install_dir"]}\\BepInEx\\plugins"),"files":[]},
	"SPT": {"root":(f"{args["spt_install_dir"]}\\SPT\\user\\mods"),"files":[]}
}
SPT_CONFIGS_FOLDER = {
	"BepInEx": {"root":(f"{args["spt_install_dir"]}\\Bepinex\\config"),"files":[]},
	"SPT": {"root":(f"{args["spt_install_dir"]}\\SPT\\user\\configs"),"files":[]}
}

# Walk directory to get mods
for r,d,_f in os.walk(SPT_MODS_FOLDER["BepInEx"]["root"]):
	if r != SPT_MODS_FOLDER["BepInEx"]["root"]: continue
	SPT_MODS_FOLDER["BepInEx"]["files"].append(d)
for r,d,_f in os.walk(SPT_CONFIGS_FOLDER["BepInEx"]["root"]):
	if r != SPT_MODS_FOLDER["BepInEx"]["root"]: continue
	SPT_CONFIGS_FOLDER["BepInEx"]["files"].append(d)
for r,d,_f in os.walk(SPT_MODS_FOLDER["SPT"]["root"]):
	if r != SPT_MODS_FOLDER["BepInEx"]["root"]: continue
	SPT_MODS_FOLDER["SPT"]["files"].append(d)
for r,d,_f in os.walk(SPT_CONFIGS_FOLDER["SPT"]["root"]):
	if r != SPT_MODS_FOLDER["BepInEx"]["root"]: continue
	SPT_CONFIGS_FOLDER["SPT"]["files"].append(d)

# Walk folders to get dict of mods and their files
mods = {}

for file in SPT_MODS_FOLDER["BepInEx"]["files"]:
	pass

for mod in mods:
	pass