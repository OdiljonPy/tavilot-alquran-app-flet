import flet as ft
from bs4 import NavigableString, BeautifulSoup



class HTML:
    # ----------------------------------------------------------------------------------------------
    """
    Supported HTML tags and attributes
    """

    class Tags:
        IMG = "img"
        UL = "ul"
        OL = "ol"
        LI = "li"
        A = "a"
        B = "b"
        STRONG = "strong"
        I = "i"
        EM = "em"
        U = "u"
        MARK = "mark"
        SPAN = "span"
        DIV = "div"
        P = "p"
        CODE = "code"
        H1 = "h1"
        H2 = "h2"
        H3 = "h3"
        H4 = "h4"
        H5 = "h5"
        H6 = "h6"
        TABLE = "table"
        TR = "tr"
        TH = "th"
        TD = "td"
        BR = "br"

    class Attrs:
        STYLE = "style"
        HREF = "href"
        SRC = "src"
        WIDTH = "width"
        HEIGHT = "height"
        TYPE = "type"

    TEXT_STYLE_DECORATION = ["underline", "line-through", "overline"]

    HEADINGS_TEXT_SIZE = {
        Tags.H1: 32,
        Tags.H2: 24,
        Tags.H3: 18,
        Tags.H4: 16,
        Tags.H5: 13,
        Tags.H6: 10,
    }

    ##UPCOMING STYLE ATTRIBUTES


"""
    style_attributes = [
            "box-shadow",
            "line-height",
            "letter-spacing",
            "word-spacing",
            "overflow",
            "position",
            "top",
            "right",
            "bottom",
            "left",
        ]
"""


def parse_html_to_flet(element):
    if element.name == HTML.Tags.DIV:
        style, align_style = get_style(element, is_a_mapping=True)

        # Map <div> to ft.Column
        main_container = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Row([], **align_style)
            if "alignment" in align_style
            else ft.Column([], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            **style,
        )
        for child in element.children:
            if child.name:
                # If there's a table,
                if child.name == HTML.Tags.TABLE:
                    # Call "html_table_to_flet()" function to display the table
                    html_table_to_flet(element, main_container)

                # Recursively parse child elements
                child_flet = parse_html_to_flet(child)
                main_container.content.controls.append(child_flet)
        return main_container

    # Heading tags
    elif element.name in HTML.HEADINGS_TEXT_SIZE.keys():
        heading_text = ft.Text(
            value=element.text, size=HTML.HEADINGS_TEXT_SIZE[element.name], alignment=ft.alignment.center
        )
        return heading_text

    # Paragraph tag
    elif element.name == HTML.Tags.P:
        style = get_style(element)
        # Map <p> to ft.Column for vertical stacking
        paragraph = ft.Column([], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        # Support for nested tags inside the <p> tag
        if element.children:
            for child in element.children:
                if child.name:
                    # Parse the nested element
                    p_child = parse_html_to_flet(child)
                    paragraph.controls.append(p_child)
                elif isinstance(child, NavigableString):
                    # Handle text content directly within the <p> tag
                    text_content = child.strip()
                    if text_content:
                        text_element = ft.Text(text_content, style=style[0], text_align=ft.alignment.center,
                        size = 40,
                        )
                        paragraph.controls.append(text_element)
        return paragraph

    # Link tag
    elif element.name == HTML.Tags.A:
        # Map <a> to ft.Text with a URL
        link = ft.Text(
            spans=[
                ft.TextSpan(
                    element.text,
                    url=element.get(HTML.Attrs.HREF),
                    style=ft.TextStyle(italic=True, color="blue"),
                )
            ],
            alignment=ft.alignment.center,
            size=40,

        )
        return link

    # Image tag
    elif element.name == HTML.Tags.IMG:
        img_style, _ = get_style(element, is_a_mapping=True)

        # Map <img> to ft.Image with a source URL
        image = ft.Container(
            content=ft.Image(src=element.get(HTML.Attrs.SRC)), alignment=ft.alignment.center, **img_style
        )
        return image

    # HTML lists
    elif element.name == HTML.Tags.UL or element.name == HTML.Tags.OL:
        # Map <ul> and <ol> to ft.Column
        list_container = ft.Column(spacing=0, alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        for i, li in enumerate(element.find_all(HTML.Tags.LI)):
            _leading = (
                ft.Text("\u2022", size=40)
                if element.name == HTML.Tags.UL
                else ft.Text(f"{i+1}", size=40)
            )
            list_item = ft.ListTile(title=ft.Text(li.text, size=40), leading=_leading)

            list_container.controls.append(list_item)
        return list_container

    # Bold Tags
    elif element.name == HTML.Tags.B or element.name == HTML.Tags.STRONG:
        bold_text = ft.Text(
            value=element.text,
            weight=ft.FontWeight.BOLD
            if element.name == HTML.Tags.B
            else ft.FontWeight.W_900,
            text_align=ft.alignment.center,
            size=40,

        )
        return bold_text

    # BR
    elif element.name == HTML.Tags.BR:
        # Use an empty container with a fixed height to simulate a line break
        line_break = ft.Container(height=10, alignment=ft.alignment.center)  # Adjust height as needed for spacing
        return line_break

    # Italic Tag
    elif element.name == HTML.Tags.I or element.name == HTML.Tags.EM:
        italic_text = ft.Text(element.text, italic=True, alignment=ft.alignment.center, size=40)
        return italic_text

    # Underline Tag
    elif element.name == HTML.Tags.U:
        underlined_text = ft.Text(
            spans=[
                ft.TextSpan(
                    element.text,
                    style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                )
            ],
            text_align=ft.alignment.center,
            size=40
        )
        return underlined_text

    # Mark Tag
    elif element.name == HTML.Tags.MARK:
        style_props, _ = get_style(element, is_a_mapping=True)

        return ft.Text(
            spans=[
                ft.TextSpan(
                    element.text,
                    style=ft.TextStyle(**style_props),
                )
            ],
            text_align=ft.alignment.center,
            size=40
        )

    # Code Tag
    elif element.name == HTML.Tags.CODE:
        return ft.Markdown(
            element.text,
            selectable=True,
            extension_set="gitHubWeb",
            code_theme="atom-one-dark",
            alignment=ft.alignment.center
        )

    # Span Tag
    elif element.name == HTML.Tags.SPAN:
        span_style = get_style(element)
        return ft.Text(spans=[ft.TextSpan(element.text, style=span_style[0])], text_align=ft.alignment.center, size=40)

    else:
        # Default to ft.Container for unrecognized elements
        container = ft.Container(alignment=ft.alignment.center)
        for child in element.children:
            if child.name:
                child_flet = parse_html_to_flet(child)
                container.content = child_flet
        return container


# ____________________________________________________________________________________________________________________________________
# Parser function for html tables


def html_table_to_flet(element, container):
    table = element.find("table", border="1")
    flet_table = ft.DataTable(columns=[], rows=[])

    if table != None:
        for row in table.find_all("tr"):
            headers = row.find_all("th")
            columns = row.find_all("td")
            if headers != []:
                for i in range(len(headers)):
                    header_text = headers[i].text
                    flet_table.columns.append(ft.DataColumn(ft.Text(header_text, size=40)))

            if columns != []:
                data_cells = []
                for i in range(len(columns)):
                    cell_text = columns[i].text
                    data_cells.append(ft.DataCell(ft.Text(cell_text, size=40)))
                flet_table.rows.append(ft.DataRow(cells=data_cells))
        container.content.controls.append(flet_table)


# ___________________________________________________________________________________________________________________________________
# Associate html inline styles to the corresponding flet style properties
# ____________________________________________________________________________________________________________________________________
html_to_flet_style_mapping = {
    "color": "color",
    "background-color": "bgcolor",
    "font-family": "font_family",
    "font-size": "size",
    "text-align": "text_align",
    "text-decoration": "decoration",
    "display": "display",
    "justify-content": "alignment",
    "margin": "margin",
    "padding": "padding",
    "border-radius": "border_radius",
    "border": "border",
    "width": "width",
    "height": "height",
}


def parse_inline_styles(style_string):
    # Parse inline styles and convert to Flet properties
    style_properties = {}
    for style_declaration in style_string.split(";"):
        if ":" in style_declaration:
            property_name, property_value = style_declaration.split(":")
            property_name = property_name.strip()
            property_value = property_value.strip()

            # Convert property_name to Flet style name if needed
            property_name = html_to_flet_style_mapping.get(property_name, None)

            if property_name:
                # Map html text-decoration values to their corresponding Flet decoration values
                deco_values = {
                    "underline": ft.TextDecoration.UNDERLINE,
                    "line-through": ft.TextDecoration.LINE_THROUGH,
                    "overline": ft.TextDecoration.OVERLINE,
                }
                # Map html justify-content values to their corresponding Flet alignment values
                alignment_values = {
                    "flex-start": ft.MainAxisAlignment.START,
                    "center": ft.MainAxisAlignment.CENTER,
                    "flex-end": ft.MainAxisAlignment.END,
                    "space-between": ft.MainAxisAlignment.SPACE_BETWEEN,
                    "space-around": ft.MainAxisAlignment.SPACE_AROUND,
                    "space-evenly": ft.MainAxisAlignment.SPACE_EVENLY,
                }

                # Convert property_value to integer if it's a digit otherwise, keep the original value
                style_properties[property_name] = (
                    int(property_value) if property_value.isdigit() else property_value
                )
                # handle decoration property
                if property_name == "decoration" and property_value in deco_values:
                    style_properties["decoration"] = deco_values[property_value]
                # handle border property
                elif property_name == "border" and property_value != None:
                    property_value = property_value.split(" ")
                    style_properties["border"] = ft.border.all(
                        property_value[0], property_value[-1]
                    )
                elif (
                    property_name == "alignment" and property_value in alignment_values
                ):
                    style_properties["alignment"] = alignment_values[property_value]

    style_properties.pop("display", None)
    return style_properties


def get_style(element, is_a_mapping: bool = False):
    alignment_props = {}
    if element.get(HTML.Attrs.STYLE):
        style_props = parse_inline_styles(element.get(HTML.Attrs.STYLE))
        if "alignment" in style_props:
            val = style_props.pop("alignment")
            alignment_props = {"alignment": val}

        _style = style_props if is_a_mapping else ft.TextStyle(**style_props)

    else:
        _style = {}
    return _style, alignment_props