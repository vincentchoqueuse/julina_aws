from django import template
import markdown

register = template.Library()


def convert_html(value):
    if value is not None:
        html = markdown.markdown(value)
    else:
        html=""
    return html

def convert_latex(value):
    if value is not None:
        html = markdown.markdown(value)
        latex=html.replace("<ul>","\\begin{itemize}").replace("<li>","\item ").replace("</li>","").replace("</ul>","\\end{itemize}").replace("<p>","").replace("</p>","")
    else:
        latex = ""
    return latex


def convert_badge(value):

    html=""
    if value is not None:
        tags=value.split(",")

        for tag in tags:
            html=html+"<span class='badge badge-info'>"+tag.replace(".","")+"</span> "

    return html


register.filter('convert_latex', convert_latex)
register.filter('convert_html', convert_html)
register.filter('convert_badge', convert_badge)
