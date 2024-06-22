all = ''' DIP : UNIT V
Image compression fundamental, 
coding in  image compression
temporal and spatial redundancy in image compression 
Error-free (Lossless) and Lossy compression. Image segmentation, 
Point-line-edge detection. 
Image gradients operator, 
canny edge detection, 
Edge linking and boundary detection, 
local processing, 
thresholding, 
variable thresholding, 
Region Growing, 
Texture Segmentation; 
Region oriented segmentation.



UNIT VI
Feature Extraction: 
Edges Canny, Sobel; 
Line detectors, 
Corners Harris, 
Orientation Histogram,
SIFT. SURF.
Scale-Space Analysis Image Pyramids, 
Haar transform. 
Decision-theoretic and structure descriptors.



Digital image fundamentals Electromagnetic spectrum and imaging, Image acquisition, image formation. Digitization-sampling and quantization, Resolution-pixel, gray scale, spatial, basic relationship between pixels. Distance measure, Mathematical operations on image, Geometrical and spatial transformation.

Intensity transformation and spatial filtering: Image enhancement, log transformation, Gam transformation, Histogram processing, Histogram matching. Special filtering- spatial correlation and convolution, generating spatial filter mask, mage smoothing. Image sharpening-Laplacian filter, Highboost filter. Edge detection gradient filter, Morphological image processing erosion, Dilation, opening and closing operations. Boundary extraction, Hole Filling, Extraction of connected components, Thinning, and thickening.

Image Restoration-Noise model, Restoration-Mean filter, Geometric filter, median filter, adaptive filter, band pass filter, Notch filter, least mean square filters. Color fundamental-RGB color model, CMY color model, HSI color model. Converting RGB to HSI and vice versa.

Filtering in Frequency domain-Preliminary concept:
Fourier series,
Fourier transform,
convolution, Sampling.
DFT.
Enhancement in frequency domain,
low pass filter, high pass filter. 
Computing
IDFT from DFT.


Image compression fundamental, coding, temporal and spatial redundancy, Error-free (Lossless) and Lossy compression. Image segmentation, Point-line-edge detection. Image gradients operator, canny edge detection, Edge linking and boundary detection, local processing, thresholding, variable thresholding, Region Growing, Texture Segmentation; Region oriented segmentation.
UNIT VI
Feature Extraction: Edges Canny, Sobel; Line detectors, Corners Harris, Orientation Histogram,
SIFT. SURF. Scale-Space Analysis Image Pyramids, Haar transform. Decision-theoretic and
structure descriptors.



AI - 3,4 units
UNIT III
(12 Hours)
Knowledge Representation: Representation and mappings, Approaches to knowledge representation: Issues in knowledge representation. Using Predicate Logic: Representing simple facts in logic, Representing instance and IS-A relationships, Computable functions and predicates, Resolution, Natural deduction, Forward vs. Backward reasoning.
UNIT IV:
(6 Hours)
Different Knowledge Representation Schemes: Semantic nets, Frames, Conceptual dependency,
Scripts






MA - 1,5,6 units






CNS : 3,4
Unit III:
(7 Contact hours)
Principles of public key crypto systems, RSA algorithm, security of RSA, key management, Diffle- Hellman key exchange algorithm, introductory idea of Elliptic curve cryptography, Elgamel encryption, Message Authentication and Hash Function: Authentication requirements, authentication functions, message authentication code, hash functions, birthday attacks, security of hash functions and MACS.
Unit IV:
(7 Contact hours)
MD5 message digest algorithm, Secure hash algorithm (SHA), Digital Signatures: Digital Signatures authentication protocols digital signature standards (DSS) proof of digital signature algorithm, Authentication Applications: Kerberos and X.509, directory authentication service, electronic mail security, pretty good privacy (PGP), S/MIME








ST - 3,4 units
UNIT-III
test case design test case design strategies: black box approach to test design, random testing, requirements based testing, boundary value analysis, equivalence class partitioning, state-based testing, cause-effect graph, compatibility testing, user documentation testing, domain testing, using white box approach to test design: test adequacy criteria, static testing vs. structural testing, code functional testing, coverage and control-flow graph, covering-code logic, paths, code-complexity testing, evaluating test-adequacy criteria. (12 Contact hours)
UNIT - IV
Levels of testing: need of levels of testing, unit testing, designing the unit tests, the test harness, running the unit tests and recording results, integration tests, designing integration tests, integration test planning.defect bash elimination system testing, acceptance testing, performance testing, regression testing, ad-hoc testing, alpha-beta tests, testing Object Oriented systems-usability and accessibility testing, configuration testing, compatibility testing, testing the documentation, website testing.'''




dip_5 = '''Image compression fundamental, 
coding in  image compression
temporal and spatial redundancy in image compression 
Error-free (Lossless) and Lossy compression. 
Image segmentation, 
Point-line-edge detection. 
Image gradients operator, 
canny edge detection, 
Edge linking and boundary detection, 
local processing, 
thresholding, 
variable thresholding, 
Region Growing, 
Texture Segmentation; 
Region oriented segmentation.'''



dip_4 = '''Filtering in Frequency domain-Preliminary concept:
Fourier series,
Fourier transform,
convolution, Sampling.
DFT.
Enhancement in frequency domain,
low pass filter, high pass filter. 
Computing
IDFT from DFT.'''

dip_6 = '''Feature Extraction
Edges 
Canny
Sobel
Line detectors,
Corners
Harris, 
Orientation Histogram,
SIFT.
SURF.
Scale-Space Analysis
Image Pyramids, 
Haar transform. 
Decision-theoretic and structure descriptors.'''


cns_3 = '''Principles of public key crypto systems, 
            RSA algorithm,
            security of RSA,
            key management,
            Diffle- Hellman key exchange algorithm,
            introductory idea of Elliptic curve cryptography,
            Elgamel encryption, 
            Message Authentication and Hash Function
            Authentication requirements,
            authentication functions,
            message authentication code,
            hash functions,
            birthday attacks,
            security of hash 
            functions and MACS.'''
cns_4 = '''MD5 message digest algorithm,
          Secure hash algorithm (SHA),
          Digital Signatures
          Digital Signatures authentication protocols 
          digital signature standards (DSS)
          proof of digital signature algorithm,
          Authentication Applications
          Kerberos and X.509
          directory authentication service
          electronic mail security
          pretty good privacy (PGP)
          S/MIME'''


ai_3 = '''Knowledge Representation
Representation and mappings
Approaches to knowledge representation
Issues in knowledge representation
Using Predicate Logic
Representing simple facts in logic
Representing instance and IS-A relationships
Computable functions and predicates
Resolution
Natural deduction
Forward vs. Backward reasoning'''




ai_4 = '''Different Knowledge Representation Schemes
Semantic nets,
Frames,
Conceptual dependency,
Scripts'''




subs = {
            "dip4":(dip_4," in Digital Image Processing"),
            "dip5":(dip_5," in Digital Image Processing"),
            "dip6":(dip_6," in Digital Image Processing"),
            "cns3":(cns_3," in Cryptography and network security"),
            "cns4":(cns_4," in Cryptography and network security"),
            "ai3":(ai_3," in Artificial Intelligence mahesh uddar"),
            "ai4":(ai_4," in Artificial Intelligence mahesh udaar"),
        }





cns_3 = '''Principles of public key crypto systems, 
Topic 2
Topic 3 
<< Remaining topics pasted here >> '''

import webbrowser
def openBrowser(text,posttext):
    query = text + posttext 
    search_url = "https://www.google.com/search?q=" + '+'.join(query.split())
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Path to Chrome executable may vary
    webbrowser.get(chrome_path).open(search_url)

def searchQuery(topics_sub):
    topics,subject = topics_sub
    for topic in topics.split("\n"):
        openBrowser(topic, subject + " Notes , Videos ,Content")
        print(topic)
searchQuery((cns_3," in Cryptography and network security"))






# searchQuery(subs["cns3"])













