from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Reds8
# from bokeh.palettes import Blues8
from bokeh.embed import components
import pandas

# Read in CSV
df = pandas.read_csv('book-sales.csv')

# book = df['Book']
# sales = df['Sales_million']

# Create ColumnDataSource from data frame
source = ColumnDataSource(df)

output_file('index.html')

# Book list
book_list = source.data['Book'].tolist()

# Add plot
p = figure(
    y_range = book_list,
    plot_width = 900,
    plot_height = 1100,
    title = 'List of Best-Selling Individual Books',
    x_axis_label = 'Approximate Sales',
    margin = 100,
    tools = 'pan,box_select,zoom_in,zoom_out,save,reset',
)


# Render glyph
p.hbar(
    y = 'Book',
    right = 'Sales_million',
    left = 0,
    height = 0.2,
    # color = "#53777a",
    fill_color = factor_cmap(
        'Book',
        palette=Reds8,
        # palette=Blues8,
        factors=book_list
    ),
    fill_alpha = 0.6,
    source = source,
    legend = 'Book'
)



# # Add legend
# p.legend.orientation='vertical'
# p.legend.location='top_right'
# p.legend.label_text_font_size='13px'


# Add Tooltips
hover = HoverTool()
hover.tooltips = """
<div>
    <h3>@Book</h3>
    <div><strong>Author: </strong>@Author</div>
    <div><strong>First Published: </strong>@First_published</div>
    <div><strong>Sales in millions: </strong>@Sales_million</div>
    <div><img src="@Image" alt="" width="250" /></div>  
</div>
"""
p.add_tools(hover)




# Show results
show(p)

# # Save file
# save(p)

# # Print div and script
# script, div = components(p)
# print(div)
# print(script)