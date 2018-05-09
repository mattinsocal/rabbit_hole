# coding: utf-8
'''
------------------------------------------------------------------------------
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
--------------------------------------------------------------------------

Matt Funk 2018
runall.py
'''

import importlib

subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

# Set raw data path
raw_data = r"./data/raw/winemag-data-130k-v2.csv"

# Set country
country = r"Chile"

def main():
    '''
    Run everything
    '''
    #src/data/01_subset-data-GBP.py data/raw/winemag-data-130k-v2.csv
    #src/visualization/02_visualize-wines.py data/interim/2018-05-09-winemag_priceGBP.csv
    #src/data/03_country-subset.py data/interim/2018-05-09-winemag_priceGBP.csv Chile

    subset_file = subset.process_data_GBP(raw_data)
    print(subset_file)
    plotwines.create_plots(subset_file)
    country_file = country_sub.get_country(subset_file, country)
    print(country_file)

    return

# MAIN =============================================
if __name__ == "__main__":

    main()
