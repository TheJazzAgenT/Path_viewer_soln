# STL_viewer_hw
## Context
At Machina Labs, we use our robots to "form" different shapes (parts) from flat sheets of metal. Typically the parts formed include sections that enable us to manufacture them, but which are not required by our clients. So, at some point, we must "cut out" the desired part from the fully built geometry. Again this is done using our robots, but this time with cutting tools mounted on them. To help us with such tasks, we have built a variety of software tools. 

The 'part' shapes or geometries are provided to us by clients in different CAD file formats. We use various off-the-shelf and in-house software tools to adapt these geometries. We have other tools to generate "forming paths" or "cutting paths" which enable our robots to "form" or "cut" parts. CAD files come in a variety of industry standard file formats, including the .STL format. For the cut-path (and forming-path), we use internally generated .CSV formatted data files. The cut-data includes a list of 3D points the robot passes through. For each point, there are X, Y and Z values corresponding to 3D co-ordinates of the point. These points will be used in this assignment. The cut-path files also include 7 other values - NX, NY, NZ, IX, IY and IZ are two orthogonal direction vectors at each point, while CUTNUM is an identifier for a specific cut (multiple cut paths may be included in a single cut-path file). These last 7 values may be ignored for the purpose of this assignment.

## Objective
Build a User Interface application that allows a user to load and view a CAD geometry along with a path showing where it is to be cut.
- The program should allow the user to provide two input files - a part .STL file and a path .CSV file. The input files may be provided as command line parameters when launching the program or via graphical controls that allow user to find and select files from the file system after program is running.
- The program should present user with a GUI that includes a viewing window, and in the window render the inputted .STL geometry.
- Viewing window should also display the cut path - in a bold (bright red?) color, and sufficient thickness to easily see it superimposed on the part.
- While the cut-path is a set of independent points, display them as a continuous path by connecting consecutive points with a straight line.
- User should be able to use mouse/touchpad and/or keyboard to manipulate the items in the viewing window.
- The user should be able to rotate the viewed items about multiple axes and be able to zoom in/out of the view.
- The program should be able to read and validate the .STL and .CSV files and notify user when a corrupt file is selected for viewing.
- Sample files have been provided - part.stl and cut_path1.csv, are a formed geometry and corresponding cut_path to separate it from the desired part.

## Requirements
- The application may run on a Windows or Linux workstation. Alternatively, it could be a web-app that uses a browser for UI. 
- Developed in the candidate's choice of programming language.
- Candidate may use and incorporate any publicly available graphics libraries for the task.
- Candidates must provide executables for functional evaluation, as well as code for review and discussion during the follow-on call. The delivered package must include any necessary configuration or other files.
- Deliverables must include documentation that could be followed to download, install and/or run the application.
- The code must be organized and well-documented. 
- The effort is expected to take between 2 - 8 hours based on the candidate’s experience in such development tasks.

## Grading Criteria
- We’re looking for code that is clean, readable, performant and maintainable.
- The developer must think through the process of deploying and using the solution and provide necessary documentation.

## Optional Challenge
Enhance the viewer application by adding the following capabilities...
- Provide graphical controls for the user to import into or remove .STL and .CSV files from the viewer, after the program is launched.
- Enable rendering of the CAD geometry in different forms (mesh/triangles, smooth surface, shaded surface, etc.)
- Allow user to import and display multiple CAD and path files simultaneously.
- Allow different path files to be displayed in different colors.

## Submission
In order to submit the assignment, do the following:

1. Navigate to GitHub's project import page: [https://github.com/new/import](https://github.com/new/import)

2. In the box titled "Your old repository's clone URL", paste the homework repository's link: [https://github.com/Machina-Labs/STL_viewer_hw](https://github.com/Machina-Labs/STL_viewer_hw)

3. In the box titled "Repository Name", add a name for your local homework (ex. `STL_viewer_soln`)

4. Set privacy level to "Public", then click "Begin Import" button at bottom of the page.

5. Develop your homework solution in the cloned repository and push it to Github when you're done. Extra points for good Git hygiene.

6. Send us the link to your repository.
