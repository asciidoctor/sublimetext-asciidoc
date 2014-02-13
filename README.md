# A New AsciiDoc Bundle for TextMate 2

## Ground of Being

The purpose of this bundle is to provide a working milieu for editing [AsciiDoc](http://asciidoc.org) in [TextMate 2](https://github.com/textmate/textmate).

Previously, I was using the [Zuckschwerdt AsciiDoc bundle](https://github.com/zuckschwerdt/asciidoc.tmbundle) for TextMate; with a few changes to add missing features and to make it less crashy, it has served me fairly well under TextMate 1, through thousands of pages and four editions of my books (currently [iOS 7 Programming Fundamentals](http://shop.oreilly.com/product/0636920032465.do) and [Programming iOS 7](http://shop.oreilly.com/product/0636920031017.do)). It had some quirks and shortcomings, but I could live with them.

Then, however, Mac OS X 10.9 ("Mavericks") arrived. This caused my Ruby-based TextMate projects (such as [RubyFrontier](https://github.com/mattneub/RubyFrontier)) to behave badly, until I also adopted TextMate 2. At that point, the old AsciiDoc bundle began to behave _very_ badly, and I decided to write my own. This is the result: a new AsciiDoc bundle, written from scratch, in which I can maintain and write my books.

## Problems, Solutions, and Philosophy

An advantage of writing the grammar entirely from scratch is that I was able to make a completely fresh start. Many of the problems with the previous AsciiDoc bundle were caused by incorrect assumptions, mostly having to do with the fact that it was based on the Markdown bundle, which was a huge mistake, as AsciiDoc is not particularly like Markdown and is certainly not related to it. For example, the previous Asciidoc bundle's grammar, copying the Markdown bundle, was scoped as `text.html.asciidoc`; this caused all kinds of havoc, because it allowed the HTML TextMate bundle to reach into the AsciiDoc bundle and affect such things as styling and indentation in a particularly horrible way. But this was quite unnecessary, because although Markdown may be said in some weird way to be based on HTML, AsciiDoc most certainly is not.

In order to write the "grammar" for this bundle from scratch, I have had to grapple with learning about TextMate grammars. This, in turn, has brought me smack dab into a major limitation of TextMate grammars: they are limited to parsing in a single pass, one line (paragraph) at a time.

That limitation means that TextMate is not at all suited to a markup "language" such as AsciiDoc. My solution is not to attempt in any way to push the limits; on the contrary, my philosophy is that the only sensible way to "solve" the problem is to content myself with doing what TextMate comfortably _can_ do, even if this means omitting aspects of AsciiDoc. For example:

* AsciiDoc can do "setext"-style headers, a line of some number of text characters, followed by a line of the same number of delimiter characters. But TextMate can't "see" a two-line combination of this sort; it sees only one line at a time, and cannot peek ahead. Thus, while TextMate can (sort of) "see" the line of delimiter characters, there is no way TextMate can know that a line of text is the line _preceding_ the line of delimiter characters — so it can't style that text, or fold on it, or include it in the document's "table of contents".

  My solution is to give up. I mark up the line of delimiter characters, but I ignore the line of text. I can do styling, folding, and "table of contents" on the _other_ style of heading (where you start the line with one or more equals signs), so if you want those features, use that style, not the "setext" style.

* Similarly, a list block in AsciiDoc is a complex thing, involving AsciiDoc's flexible notion of a paragraph (it can include newline characters) as well as an awareness of what kind of paragraph comes before and after. TextMate can't grapple with any of that. So I don't even try. I can pick out pretty reliably the characters that signal the _start_ of an individual list paragraph, so I mark them — and that's all.

## Details

I have tried to make the "grammar" (which visibly styles the syntactically significant pieces of the text) reasonably complete; I have certainly brought it to the point where it marks up my own book chapters very well indeed. But, as I've just explained, I can't make TextMate parse the document the way AsciiDoc does. Therefore, to use this bundle, you have to know some special rules and differences that distinguish my limited version of AsciiDoc from real AsciiDoc.

* As I explained in the previous section, you should **avoid setext headers**: use `#`-headers instead. Moreover, AsciiDoc has various styles of `#`-header, but I support only the style where the line _starts_ with `#`. If you use this style, you get nice markup, section folding, and a hierarchical table of contents.

* My **table of contents** includes only two kinds of thing: `#`-style headers, and "known" section templates such `appendix` and `index`. Such section templates must be _explicit_; I do not parse header text to deduce the section type the way AsciiDoc does.

* TextMate can't see across line boundaries. This is a severe problem, because an AsciiDoc paragraph can consist of multiple lines. In order to keep things simple, fast, and coherent, therefore, all **inline markup** such as quotes _must be confined to a single line_ (i.e. no explicit linefeed in the middle) if you want them marked up. Thus:

        This will be *bold*.
        And this will be _italic_.
        But this will be _neither *bold
        nor* italic_ even though in AsciiDoc it is.

  This is not a severe limitation, and the result is _way_ better than the previous AsciiDoc bundle, which fell into all kinds of incoherencies over this sort of thing.

* **Single-quoted strings** (single backtick on the left, single apostrophe on the right) are _not coded for at all_. You can use them, of course, but I don't mark them up. AsciiDoc itself is already incoherent in this regard, especially when single-quoted and double-quoted strings appear in the same paragraph, and it just isn't a complication I want to get into. In my own writing, I explicitly surround single-quoted strings with curly quotes (‘like this’), and these are a smart typing pair, so it shouldn't be a big deal.

* **Comment blocks** can be folded, but only if you follow this very specific rule: the opening delimiter is a line consisting of exactly five slashes (`/`), and the closing delimiter is a line consisting of exactly four slashes and a space. The reason is that TextMate can't do folding unless the opening and closing delimiters _differ_, so I have had to make up an artificial difference. (Naturally, if you use the included snippet, `com[TAB]`, that is what I give you.)

* **Sidebar blocks** work like comment blocks (see previous paragraph): they can be folded, if the opening delimiter is exactly five asterisks (`*`) and the closing delimiter is exactly four asterisks and a space. (Naturally, if you use the included snippet, `side[TAB]`, that is what I give you.)

* An **example block** delimiter can only have four or five equal signs (`=`), because otherwise TextMate can't distinguish it from a level 0 setext header delimiter (which is assumed to be longer). (Naturally, if you use the included snippet, `ex[TAB]`, that is what I give you.)

* Similarly, a **passthrough block** delimiter can only have four or five plus signs (`+`), because otherwise TextMate can't distinguish it from a level 4 setext header delimiter (which is assumed to be longer). (Naturally, if you use the included snippet, `pass[TAB]`, that is what I give you.)

* Similarly, a **code (listing) block** delimiter can only have four or five hyphens (`-`), because otherwise TextMate can't distinguish it from a level 1 setext header delimiter (which is assumed to be longer). (Naturally, if you use the included snippet, `code[TAB]`, that is what I give you.)

  (By the way, a listing block is assumed to contain source code, but no assumption is made about language so you won't see any syntax coloring.)

* **Bulleted and numbered paragraphs** are picked out solely on the basis of the fact that they start with a bullet or number (in the various manifestations that AsciiDoc permits), and that bullet or number is the only thing about them that I mark up. This means you can get a false positive if you start right after a hard wrap with a bullet or number appropriately formatted. This does no harm and is easily avoided.

* **Macros** are notated only if you use the form of notation containing a colon (or two colons) and ending in square brackets.

* **Passthrough** blocks, `pass:` macros, and `+++` and `$$` delimited passthrough are assumed to contain XML (i.e. the XML grammar is injected at this point). In my usage this is always true, so it is a reasonable assumption, and it shouldn't get badly in the way in other cases.

* I have not coded at all for **tables**.

## Current Usage and Future Directions

I wrote this bundle because I wanted a working AsciiDoc bundle in order to continue using TextMate 2 and AsciiDoc under Mavericks as my writing tool. The result is something that works for me. In my opinion this AsciiDoc TextMate bundle is better than any other that I've seen. I am able to write in an agile fashion, and the text is marked up in a way that looks clean and informative under the Theme that I particularly favor (Mac Classic).

Nonetheless, there may be areas in which I have fallen short just because I'm not conscious of them. For example, I have probably not done a sufficiently complete list of includes for my sidebar block, because I stopped after I had included everything I actually use in sidebars. If you have suggestions, feel free to let me know. If you are the kind of person who can grapple with the nitty-gritty of TextMate grammars, feel free to fork and/or to submit a pull request.

Matt Neuburg, <http://www.apeth.net/matt/default.html>