
# User Profile Picture Bulk Upload for Incident IQ

I've created a barebones Python script for uploading user profile pictures in bulk using the Incident IQ API.  Please note this is using an **undocumented** API call so it may or may not continue to work in the future.

# Requirements

 - Python 3 (tested with 3.10.7 on Windows)
 - User profile pictures stored locally
	 - Must be in jpg format, recommend 150px by 150px in size
	 - File name must equal the school id (ex. 123456.jpg)
- [Git](https://git-scm.com/download/win) (if using autocrop)

>For best results, I highly recommend using [autocrop](https://github.com/leblancfg/autocrop) to crop and resize the photos.  I included my customized version in the requirements-autocrop.txt file.

# Setup

 1. Clone this repo
 2. Create a Python virtual environment (`python -m venv venv`)
 3. Activate your venv (`venv\scripts\activate`)
 4. Install dependencies (`pip install -r requirements.txt`)
 5. In the uploadpics.py file, edit the constants at the top with your IIQ tenant's data
 6. (Optional) If your photos are not yet cropped, you can add autocrop to your python environment by running `pip install -r requirements-autocrop.txt`.

# Usage

There are no command line parameters.  Simply run:
`python uploadpics.py`

A log file will be created in the same directory as the script, as well as displayed in your console window.

Also included is `facedetect.py`.  This allows you to test how the autocrop function works on a single image.  To use, put an image file in the same directory as this script, then change the filename on line 36 in `facedetect.py`.  Running `python facedetect.py` will show you how the crop will work.

# Notes

I used this script to upload around 20k pictures.  However it did crash twice during the process, possibly due to being rate limited on API calls.  Just something to be aware of.

Thank you to the IIQ developers for making such a robust API!
