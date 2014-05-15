import json
import sys
from netCDF4 import Dataset
import scipy.ndimage.interpolation as i


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: %s gebco_nc" % sys.argv[0]
        sys.exit(1)
    
    gebco = Dataset(sys.argv[1], "r")
    dims = gebco.variables['dimension'][:]
    grid_data = gebco.variables['z'][:].reshape(dims[1], dims[0])
    ratio = 500.0 / dims[0]
    gebco_downscaled = i.zoom(grid_data, ratio)
    
    with open("data.js", "w") as f:
        f.write("var elevation =" + json.dumps(gebco_downscaled.tolist()) + ";")
