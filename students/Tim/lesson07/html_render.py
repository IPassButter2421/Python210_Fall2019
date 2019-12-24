#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    Tag = 'html'
    
    def __init__(self, content=None, **kwargs):
        self.Content = []
        self.Content.append(content)
        self.attributes = kwargs
        pass

    def append(self, new_content):
        if new_content == '':
            self.Content.append("\t")
        else:
            self.Content.append(new_content)
        pass

    def render(self, out_file):
        #loop through the list of contents
        if self.attributes:         
            open_tag = ["<{}".format(self.Tag)]      
        else:
            out_file.write("<{}>\n".format(self.Tag))
            
        for content in self.Content:
            if content is None:
                pass
            else:
                try:
                    content.render(out_file) #this is the recursive calls down
                except AttributeError:
                    if self.attributes:
                        for key in self.attributes.keys():
                            open_tag.append(' {}="{}"'.format(key, self.attributes[key]))
  
                        open_tag.append(">\n")
                        out_file.write("".join(open_tag))

                    out_file.write(content)#this catches the end of recursion and works backwards
                    out_file.write("\n")

        out_file.write("</{}>\n".format(self.Tag))
        
class Html(Element):
    Tag = 'html'

class Body(Element):
    Tag = 'body'

class P(Element):
    Tag = 'p'
        
class Head(Element):
    Tag = 'head'
    
class OneLineTag(Element):
    
    def render(self, out_file):
        out_file.write("<{}>".format(self.Tag))
        out_file.write(self.Content[0])
        out_file.write("</{}>\n".format(self.Tag))
    #Protection of manipulating append method
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    Tag = 'title'
    
class SelfClosingTag(Element):
    
    def render(self, out_file):
        out_file.write("<{}".format(self.Tag))
        for content in self.Content:
            if content is None:
                pass
            else:
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(content)
                    for key in self.attributes.keys():
                        out_file.append(' {}="{}"'.format(key, self.attributes[key]))
        out_file.write(" />\n".format(self.Tag))
        print(out_file)
        assert False
    
    def append(self, content):
        raise NotImplementedError
       

class Hr(SelfClosingTag):
    Tag = 'hr'
        
