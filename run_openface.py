import glob
import subprocess
import os

directories = glob.glob("images/*")
output = "output"

for dir in directories:
    output_dir = "%s/%s" % (output, dir)
    os.makedirs(output_dir)
    process = subprocess.Popen(["build/bin/FeatureExtraction", "-fdir", dir, "-out_dir", output_dir])
    process.wait()
