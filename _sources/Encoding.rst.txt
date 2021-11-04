**********************************
Encoding Unicode: UTF-8 vs. UTF-16
**********************************
Before Unicode
==============
Basics of Text Encoding and ASCII
---------------------------------
A human perceives a text as an arrangement of letters. Spaces between letters help us to recognize words, and words have their specific meanings. Computers deal with texts in a different way. They treat letters, digits, punctuation marks and whitespaces as characters, and process them in the form of bits. A bit is a basic unit of information that shows a logical state and has one of two possible values. These values are commonly represented as “0” and “1”.

Here is the word *hello* represented in 0’s and 1’s:

01101000 01100101 01101100 01101100 01101111

A character encoding standard, or simply **encoding**, allows all computers to record characters as bits and read them in the same way.

:Encoding: a set of rules for converting texts from one representation to another.

In 1963 the first version of **The American Standard Code for Information Interchange (ASCII)** was published. It described 7-bit codes for 128 characters including digits, lowercase and uppercase Latin letters, punctuation symbols, non-printing characters, and control codes.

Here are the letters of *word* with their ASCII codes in binary:

+---+----------+
| w | 01000001 |
+---+----------+
| o | 01000010 |
+---+----------+
| r | 01000011 |
+---+----------+
| d | 01000100 |
+---+----------+

This table is a simplified example of a **code page**.

:Code page: a table where characters are assigned to specific bit sequences.

Although ASCII in usually associated with binary representation, a bit sequence can be represented in any numerical system.

Here are the ASCII codes of *hello* in hexadecimal:

68 65 6C 6C 6F

In ASCII each character is coded by 7 bits, while a byte consists of 8 bits. It means that the left-most bit is always “0”. Making the left-most bit meaningful allows to double the number of available codes. And that was done to include letters of languages other than English. But 256 codes were still not enough for the characters of all existing languages to be put in one single code page. That is why numerous code pages for different languages and their combinations appeared.

Single-Byte Character Encodings
-------------------------------
Most of national code pages use exactly one byte to encode each graphic character. They are commonly referred to as **single-byte character set (SBCS)** encodings.

:Character set or charset: a set of characters that can be encoded.

E.g., the charset of ASCII is limited to 128 characters, while single-byte charsets can include up to 256 characters.

.. important:: * An **encoding** is a set of rules for text conversion
          * A **code page** is a table that assigns codes to characters
          * A **character set** is a set of characters that can be encoded

These three terms are very often used interchangeably. But it is important to keep in mind their exact definitions for a better understanding of text conversion procedures.

Single-byte character sets were in common use in 1980’s and 1990’s, and their support is still available in Windows and other platforms. SBCS encodings (e.g., Windows-1252, KOI8-R, ISO/IEC 8859, etc.) are extended ASCII code pages as their first 128 codes are similar to ASCII. They are also referred to as *Windows code pages*.

Here are the common issues and limitations of these encodings:

* They encode only 256 symbols including 128 codes reserved for ASCII characters
* System fonts must support a specific encoding
* Converting one encoding into another causes partial losses 
* Specific fonts must be provided when exchanging files between different platforms
* Asian languages with thousands of characters cannot be supported

Two and More Bytes Per Character
--------------------------------
One byte is not enough to encode texts in languages that use more than 256 unique characters. It is the case for most Asian languages, including Chinese, Japanese, Korean etc. Two bytes allow assigning codes to 65,536 different characters. **Double-byte character sets** (e.g., BIG-5, Shift JIS) use 2 bytes (16 bits) per character.

.. note:: There can be several encodings for one language featuring different character sets and encoding methods. For example, BIG-5 covers mostly traditional Chinese, while GB18030 supports both Traditional Chinese and Simplified Chinese ideographs.

There are also **triple-byte charsets (TBCS)** and **multi-byte charsets (MBCS)** with three and more bytes per character.

The Unicode Standard
====================
That is how a plenty of national encodings came up. To make things worse, if someone needed to mix, for example, Slovenian and Swedish in the same text, he had no choice but to create a new encoding. That resulted in countless encodings. It was not possible to read a text file unless the original encoding was known and present in the system.

The global development of World Wide Web made it evident that people all over the world want to communicate in their national languages. The text data in all these languages must be properly encoded, transmitted and decoded by various software, systems and devices all over the world.

In 1987 a group of enthusiasts started work on an international and multilingual character encoding system. The idea was to provide codes for all characters of all living languages, create a unified table, and develop universal encoding/decoding methods.

In 1991 the Unicode Consortium published the first version of Unicode. At that time, the standard used a 16-bit design. Such a choice was based on the assumption that 2 bytes is enough to encode all characters in modern use, while all others do not need to be included.

.. note:: The Unicode Consortium is a non-profit organization incorporated in 1991 in California. Its mission is to maintain and update the Unicode Standard.

Since 1996, when Unicode 2.0 came up, the character set is not limited to 16 bits. That allowed to include historical scripts, rare characters, emojis and a plenty of other symbols.

Version 13.0 was released in March 2020 adding 4,969 CJK (Chinese-Japanese-Korean) unified ideographs, some graphic characters, 55 emojis, etc.

Basics of Unicode
-----------------
Unicode is a standard that includes character encodings along with code charts, reference data files, character properties and rules.

.. important:: Unicode is **NOT** an encoding.

The current version of the standard supports the **Unicode Transformation Format (UTF)** encodings: UTF-8, UTF-16, and UTF-32. The first two are the most commonly used ones.

Unicode defines a **codespace** of numerical values ranging from 0 to 10FFFF called **code points**. Each code point is denoted as ‘U+’ plus the code point value in hexadecimal. The numeric value must be at least 4 digits long. For smaller numbers leading zeros must be added. E.g. a Latin small letter ‘x’ takes the 78th position in Unicode chart and is denoted as U+0078.

The Unicode codespace is divided into 17 **planes**, numbered 0 to 16. Each plane consists of 65,536 (2\ :sup:`16`) code points. Plane 0 is called **Basic Multilingual Plane (BMP)** and contains the most commonly used characters. All Unicode planes can accommodate 1,114,112 code points. Besides the current repertoire of 143,859 characters they contain 2,048 surrogates, 66 non-characters, and 137,468 private-use characters. There are also 830,606 reserved code points, which are not assigned but available for use.

It is essential to distinguish between the following concepts:

* a *user-perceived character*
* a *code point* assigned to a character by Unicode
* a *sequence of bytes* used to store the code of a character in memory

Check out the following table:


+------------------------------+---------------+------------+-------------+-----------+
| Description                  | Visual output | Code point | Sequence of bytes       |
+==============================+===============+============+=============+===========+
|                              |               |            | **UTF-8**   | **UTF-16**|
+------------------------------+---------------+------------+-------------+-----------+
| SMILING FACE WITH SUNGLASSES | 😎            | U+1F60E    | f0 9f 98 8e | d83d de0e |
+------------------------------+---------------+------------+-------------+-----------+
| ARABIC LETTER HAMZA          | ء             | U+0621     | d8 a1       | 0621      |
+------------------------------+---------------+------------+-------------+-----------+
| LATIN SMALL LETTER I         | i             | U+0069     | 69          | 0069      |
+------------------------------+---------------+------------+-------------+-----------+

The table clearly shows that the sequence of bytes depends on the encoding.

UTF-8
-----
The name of this encoding derives from *Unicode Transformation Format – 8-bit*.  8-bit refers to the length of each **code unit**.

:Code unit: the unit of storage of a code point.

A code point can be encoded with one or several code units. UTF-8 is a variable length character encoding. It uses one code unit for each of the first 128 code points, and up to 4 code units for each of the subsequent ones. In other words, a Unicode character in UTF-8 occupies from 1 to 4 bytes of disk space.

A character can be encoded with 1, 2, 3, or 4 code units. The number of code units or bytes in each specific encoded character can be detected by one or several highest bits as follows:

+-------------------------+-------------------------------------+
| Unicode code points     | Bit mask in UTF-8                   |
+=========================+=====================================+
| 0000-007F (7 bits)      | 0xxxxxxx                            |
+-------------------------+-------------------------------------+
| 0080-07FF (11 bits)     | 110xxxxx 10xxxxxx                   |
+-------------------------+-------------------------------------+
| 0800-FFFF (16 bits)     | 1110xxxx 10xxxxxx 10xxxxxx          |
+-------------------------+-------------------------------------+
| 010000-10FFFF (21 bits) | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |
+-------------------------+-------------------------------------+

This is how UTF-8 encodes U+0621 (ARABIC LETTER HAMZA) into *d8 a1*:

0621 belongs to the range 0080-07FF, so it will take 11 bits and two code units to encode it

#. Convert “0621” into binary
     * 0621 --> 11000100001.
#. Apply the 10xxxxxx mask to the bits numbered 0-6 (starting from the right-most bit) to get the second byte
     * _ _ _ _ _ 100001 --> 10100001
#. Apply the 110xxxxx mask to the remaining five bits to get the first byte
     * 11000 _ _ _ _ _ _ --> 11011000
#. Convert 11011000 10100001 into hexadecimal
     * 11011000 10100001 --> d8 a1.

.. important:: UTF-8 is a self-synchronizing encoding.

A byte of the 10xxxxxx form is called a *continuation byte*. You can start decoding from any point – just skip over continuation bytes until it is a non-continuation one. That will be the beginning of the byte sequence of a specific code point.

The first 128 code points of Unicode are similar to ASCII characters and include Latin letters, punctuation marks, digits and special characters. Each of them is encoded in UTF-8 with a single byte. Which means that HTML markup, CSS, URLs, etc. are encoded in the most efficient way. That significantly decreases the size of a webpage.

Those 128 code points are encoded with the same byte sequences as in ASCII and cannot be decoded wrong. Thus, UTF-8 is completely safe to use with programming and mark-up languages that process certain ASCII symbols in a specific way.

UTF-16
------

The code unit in UTF-16 encoding is 16 bits long. It is also a variable length encoding, but unlike UTF-8 there are either 2 or 4 bytes per character. UTF-16 is commonly used for text strings in Microsoft Windows, Java, C#, and some other applications.

One or two 16-bit code units in UTF-16 allow to encode the whole Unicode codespace. UTF-16 encodes each code point in the range U+0000-U+FFFF with a single byte. This range covers the characters of the most common languages and writing systems.

The code points in the range from U+10000 to U+10FFFF are encoded by UTF-16 in the form of surrogate pairs. 

:Surrogate pair: two 16-bit code units in UTF-16.

According to the Unicode standard, the code points within the range U+D800–U+DFFF are excluded from BMP and used to create surrogate pairs in UTF-16.

This is how to create a surrogate pair for Unicode Han Character U+22023 in UTF-16:

#. Substract 10000 from the code point
    * 22023 – 10000 = 12023 (hexadecimal) –> 0001001000 0000100011 (binary, 20 bits)
#. Add the high ten bits to D800
    * 0001001000 (binary) –> 48 (hexadecimal) + D800 = D848
    * That is the first 16-bit code unit or high surrogate
#. Add the low ten bits to DC00
    * 0000100011 (binary) –> 23 (hexadecimal) + DC00= DC23
    * That is the second 16-bit code unit or low surrogate
#. The high surrogate and the low surrogate form the surrogate pair
    * d848 dc23

The ranges of high surrogates and low surrogates are excluded from the BMP. The first byte of a surrogate pair can never be decoded as a BMP code point. On the other hand, two consecutive code points can never be taken for a surrogate pair.

Check out the decoding procedure for *d803 de62*:

.. important:: In computing, bits are numbered from right to left. The right-most bit is the bit 0.


#. Check the value of the bit 9 to decide if the surrogate is high/low
    * D803 –> 1101100000000011 – the bit 9 is 0, it is a high surrogate
    * DE62 –> 1101111001100010 – the bit 9 is 1, it is a low surrogate


#. The high six bits are meaningless – they only indicate that it is a surrogate. Remove them from each surrogate and make up a 20-bit sequence
    * 1101100000000011 1101111001100010 --> 0000000011 1001100010

#. Add 10000 in hexadecimal to get the code point in Unicode
    * 0000000011 1001100010 -> e62
    * E62 + 10000 = 10E62
    * U+10E62 – RUMI DIGIT THREE

Byte Order in UTF-16
--------------------
The encoded characters in the examples above are represented as sequences of bytes. But a computer stores such sequences in memory and reads them in a specific way which depends on the endianness of the particular system architecture. There are **big-endian (BE)** and **little-endian (LE)** systems.
Big-endian systems store the most significant byte at the smallest memory address. The clearest example is how we write down Arabic numerals.

.. note:: Big-endian byte order is a standard for network protocols, IBM, SPARC and Motorola processors. It is sometimes referred to as *network byte order* or *Motorola byte order*.

A big-endian system will store *d848 dc23* as “d8 48 dc 23”.

Little-endian architecture, in contrast, stores the least significant byte at the smallest address. Like as if we wrote down an Arabic numeral 123 as “321”.

.. note:: Most x86 processors use little-endian byte order and it is often called *Intel byte order*.

A little-endian system will store *d848 dc23* as “48 d8 23 dc”.

In UTF-16 the byte order is specified by a **Byte Order Mark (BOM)**. 

:Byte Order Mark (BOM): an U+FEFF code point recorded as the first character in text.

In Unicode U+FEFF stands for the invisible zero-width non-breaking space (ZWNBSP).

If the first byte is read as U+FEFF, it means that the decoder has the same architecture as the encoder and the whole text must be decoded regularly. But if it is U+FFEF, which is a non-character in Unicode, bytes must be swapped in the remaining code units.

The byte order can also be designated by the name of the encoding. If the encoding is specified as UTF-16LE or UTF-16BE, it means that the byte order is little-endian or big-endian respectively. In this case a BOM must not be present and U+FEFF must be decoded as ZWNBSP. However, most applications still ignore U+FEFF when it is the first character in a text.

UTF-8 vs. UTF-16 in Software Development
========================================
To reveal the pros and cons of these two encodings in a more explicit way, let us consider them with regard to specific software development environments.

Microsoft Windows-based architecture
------------------------------------
Win32 API, which is common for modern editions of Microsoft Windows, supports two methods of text representation: traditional 8-bit Windows code pages and UTF-16. The reasons for that are rather historical than objective. Windows 10 supports UTF-8 as a code page, but its internal encoding is UTF-16LE.

.. hint:: To interoperate with Windows APIs, you may convert between UTF-8 and UTF-16 by using  `MultiByteToWideChar <https://docs.microsoft.com/en-us/windows/desktop/api/stringapiset/nf-stringapiset-multibytetowidechar>`_ and `WideCharToMultiByte <https://docs.microsoft.com/en-us/windows/desktop/api/stringapiset/nf-stringapiset-widechartomultibyte>`_ functions.

Starting from Windows Version 1903 (May 2019 Update) Microsoft recommends using UTF-8 character encoding for web applications to ensure optimal compatibility, minimize localization bugs, and reduce testing costs.

Web and Linux
-------------
In Web and Linux environments UTF-8 is commonly used and treated as the best encoding for Unicode. C++ code, HTML\\XML tags, filesystem paths, variables and parameters consist predominantly of ASCII characters, which is one byte per character in UTF-8. That provides for efficient traffic and memory usage and improves the overall performance significantly. UTF-8 totally dominates the World Wide Web. Over 95% of websites in 2020 use this encoding. For certain languages this value is close to 100%.

There is a popular misconception that UTF-8 is only more efficient for English texts. It is true that UTF-16 could save up to 50% for an abstract Chinese text compared to UTF-8, as each code point would take two bytes instead of four. But in real world plain texts rarely exist independently without any meta-data, which is efficiently encoded by UTF-8. The actual gain of using UTF-16 will be far less than 50%, while highly probable compatibility issues will definitely ruin the perceived advantage.

Conclusion
==========
Unicode is a globally recognized standard. It is unreasonable and virtually impossible to ignore it in software development. Text strings used internally within each separate application may have any format. The only condition is proper support of the whole Unicode codespace and lossless data exchange with external modules or APIs.

When it comes to the choice of a specific Unicode encoding, it is essential to consider all relevant factors. These are system architecture requirements, use cases, customer requirements, software development workflow, etc. The decision must be taken at a very early stage and implemented by all contributors to the development process.
