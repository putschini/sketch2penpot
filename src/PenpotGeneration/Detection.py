import svgutils.transform as sg

import svgutils as svg

import sys, os, shutil, zipfile, json

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def get_basic_element_path( element_str ):
    return APP_ROOT + "/BasicElements/" + element_str + "/elements.svg"

def get_basic_element_components( element_str ):
    return sg.fromfile(APP_ROOT + "/BasicElements/" + element_str + "/components.svg" )

def move( component_str, element_str , positionx_str, positiony_str ):
    component_str = component_str.replace(element_str + "_position_x", positionx_str)
    component_str = component_str.replace(element_str + "_position_y", positiony_str)
    return component_str

def move_text( component_str, positionx, positiony, height = 16, width = 0 ):
    component_str = component_str.replace("label_position_x", str(positionx))
    component_str = component_str.replace("label_position_y", str(positiony))
    positiony = positiony + height
    component_str = component_str.replace("text_position_x", str(positionx))
    component_str = component_str.replace("text_position_y", str(positiony))
    return component_str

def resize( component_str, element_str , height_str, width_str  ):
    component_str = component_str.replace( element_str + "_height", height_str )
    component_str = component_str.replace( element_str + "_width", width_str )
    return component_str


def resize_text( component_str , height, width ):
    component_str = component_str.replace( "label_height", str(height))
    component_str = component_str.replace( "label_width", str(width))
    # height = int(height)
    # height -= int(height / 8)
    # width = int(width)
    # width -= int(width/10)
    component_str = component_str.replace( "text_height", str(height))
    component_str = component_str.replace( "text_width", str(width))
    component_str = component_str.replace("text_font_size", str(height))
    return component_str

def move_button( button_str, positionx, positiony, height, width ):
    button_str = move( button_str, "background", str(positionx), str(positiony) )
    positionx_str = positionx + ( width / 3 )
    positiony_str = positiony + ( height / 3) 
    button_str = move_text( button_str, positionx_str, positiony_str )
    return button_str

def resize_button( button_str , height, width ):
    button_str = resize( button_str, "background", str(height), str(width) )
    return button_str

def move_checkbox( checkbox_str, positionx, positiony, height, width ):
    checkbox_str = move( checkbox_str, "rectangle", str(positionx), str(positiony) )
    positionx_str = positionx + ( height + 16 )
    positiony_str = positiony + ( height / 3)
    checkbox_str = move_text( checkbox_str, positionx_str, positiony_str )
    return checkbox_str

def resize_checkbox( checkbox_str , height, width ):
    checkbox_str = resize( checkbox_str, "rectangle", str(height), str(height) )
    return checkbox_str

def move_image( image_str, positionx, positiony, height, width ):
    image_str = move( image_str, "image", str(positionx), str(positiony) )
    return image_str

def resize_image( image_str , height, width ):
    image_str = resize( image_str, "image", str(height), str(width) )
    return image_str

def move_label( label_str, positionx, positiony, height, width ):
    label_str = move_text( label_str, positionx, positiony, height, width )
    #label_str = move_text( label_str, positionx, positiony )
    return label_str

def resize_label( label_str , height, width ):
    label_str = resize_text(label_str, height, width)
    label_str = resize( label_str, "label", str(height), str(width) )
    return label_str

def move_listpicker( listpicker_str, positionx, positiony, height, width ):
    listpicker_str = move( listpicker_str, "rectangle", str(positionx), str(positiony) )
    listpicker_str = move( listpicker_str, "arrow", str(positionx + (width - 40)), str(positiony + (height / 3)) )

    positionx_str = positionx + 16
    positiony_str = positiony + ( height / 4)
    listpicker_str = move_text( listpicker_str, positionx_str, positiony_str )
    return listpicker_str

def resize_listpicker( listpicker_str , height, width ):
    listpicker_str = resize( listpicker_str, "rectangle", str(height), str(width) )
    return listpicker_str


def move_map( map_str, positionx, positiony, height, width ):
    map_str = move( map_str, "map", str(positionx), str(positiony) )
    return map_str

def resize_map( map_str , height, width ):
    map_str = resize( map_str, "map", str(height), str(width) )
    return map_str


def move_slider( slider_str, positionx, positiony, height, width ):
    positiony += (height / 2)
    slider_str = move( slider_str, "full_track", str(positionx), str(positiony - (height / 4)) )
    slider_str = move( slider_str, "track", str(positionx), str(positiony - (height / 4)) )
    positionx += (width / 2)
    positiony -= (height / 6 )
    slider_str = move( slider_str, "handle", str(positionx), str(positiony) )
    return slider_str

def resize_slider( slider_str , height, width ):
    slider_str = resize( slider_str, "full_track", str(height / 4), str(width) )
    slider_str = resize( slider_str, "track", str(height / 4), str(width / 2) )
    slider_str = resize( slider_str, "handle", str(height / 3), str(height / 3) )
    return slider_str


def move_switch( switch_str, positionx, positiony, height, width ):
    switch_str = move( switch_str, "rectangle", str(positionx), str(positiony) )
    positiony += (height / 2)
    positionx += (height / 2)
    switch_str = move( switch_str, "ellipse", str(positionx), str(positiony) )
    return switch_str

def resize_switch( switch_str , height, width ):
    switch_str = resize( switch_str, "rectangle", str(height), str(width) )
    switch_str = resize( switch_str, "ellipse", str((height / 4 * 3) / 2), str((height / 4 * 3) / 2 ) )
    return switch_str


def move_textbox( textbox_str, positionx, positiony, height, width ):
    textbox_str = move( textbox_str, "rectangle", str(positionx), str(positiony) )
    positionx_str = positionx + 16
    positiony_str = positiony + ( height / 3)
    textbox_str = move_text( textbox_str, positionx_str, positiony_str )
    return textbox_str

def resize_textbox( textbox_str , height, width ):
    textbox_str = resize( textbox_str, "rectangle", str(height), str(width) )
    return textbox_str


def create_element( type_str, center_x, center_y, height, width ):
    element_str = open( get_basic_element_path(type_str) , "r").read()

    match type_str:
        case "Button":
            element_str = move_button( element_str, center_x, center_y, height, width )
            element_str = resize_button( element_str, height, width )
        case "CheckBox":
            element_str = move_checkbox( element_str, center_x, center_y, height, width )
            element_str = resize_checkbox( element_str, height, width )
        case "Image":
            element_str = move_image( element_str, center_x, center_y, height, width )
            element_str = resize_image( element_str, height, width )
        case "Label":
            element_str = move_label( element_str, center_x, center_y, height, width )
            element_str = resize_label( element_str, height, width )
        case "ListPicker":
            element_str = move_listpicker( element_str, center_x, center_y, height, width )
            element_str = resize_listpicker( element_str, height, width )
        case "Map":
            element_str = move_map( element_str, center_x, center_y, height, width )
            element_str = resize_map( element_str, height, width )
        case "Slider":
            element_str = move_slider( element_str, center_x, center_y, height, width )
            element_str = resize_slider( element_str, height, width )
        case "Switch":
            element_str = move_switch( element_str, center_x, center_y, height, width )
            element_str = resize_switch( element_str, height, width )
        case "TextBox":
            element_str = move_textbox( element_str, center_x, center_y, height, width )
            element_str = resize_textbox( element_str, height, width )     
        case _:
            print("Element " + type_str + " not found!" )
            return

    return sg.fromstring(element_str).find_id( "shape-" + type_str + "_group_id" )



from roboflow import Roboflow
rf = Roboflow(api_key="XrtRKUfqrlykWQKHe4ta")
project = rf.workspace().project("sketch2penpot")
model = project.version(2).model


screen_size = {
    "width" : 720, 
    "height" : 1280 
    }

def get_scale( element ):
    scale = {"x" :0, "y": 0}
    scale["x"] = screen_size["width"] / element["width"]
    scale["y"] = screen_size["height"] / element["height"]
    return scale

def get_offset( element ):
    offset = {"x" :0, "y": 0}
    offset["x"] = element["x"] - ( element["width"] / 2 )
    offset["y"] = element["y"] - ( element["height"] / 2 )
    return offset


components_array = []
files_name_array = {}

def build_components( folder_path ):
    components_array.clear()
    screen_components = get_basic_element_components("Screen")
    for comp in components_array:
        if comp == "Image" or comp == "Map" or comp == "Label":
            continue
        new_comp = get_basic_element_components(comp)
        screen_components.append(new_comp)
    screen_components.save(  folder_path + "/final/" + "components.svg")


def predict_folder( folder_path ):
    files_name_array.clear()
    count = 0
    original_path = folder_path + "/original/"
    for file in os.listdir( original_path ):
        if not file.endswith(".jpg") and not file.endswith(".png"):
            continue

        file_name = file[:-4]
        print("Init Prediction")
        prediction = model.predict( original_path + file, confidence=40, overlap=10)
        prediction.save(folder_path + "/preview/" + file_name + ".jpg" )
        print("Prediction done!")

        print("Init generation")
        prediction_json = prediction.json()

        scale = {"x" :1, "y": 1}
        offset = {"x" :0, "y": 0}

        screen = sg.fromfile(get_basic_element_path("Screen"))

        #Get Screen sizes and calculate offset and scale
        for element in prediction_json["predictions"]:
            if element["class"] == "Screen":
                scale = get_scale(element)
                offset = get_offset(element)
                # print("Screen:")
                # print("   Size: " + str(element["x"] - offset["x"]) + ":" + str(element["y"] - offset["y"]))
                # print("   Scale: " + str(scale["x"]) + ":" + str(scale["y"]))
                # print("   Offset: " + str(offset["x"]) + ":" + str(offset["y"]))
                break

        # Build elements based on prediction
        for element in prediction_json["predictions"]:
            if element["class"] == "Screen":
                continue
            element_offset = get_offset(element)
            element_x = (element_offset["x"] - offset["x"]) * scale["x"]
            element_y = (element_offset["y"] - offset["y"]) * scale["y"]
            element_width = element["width"] * scale["x"]
            element_height = element["height"] * scale["y"]

            if element_x + element_width > screen_size["width"]:
                element_width -=  (element_x + element_width) - screen_size["width"]

            if element_y + element_height > screen_size["height"]:
                element_height -=  (element_y + element_height) - screen_size["height"]

            element_svg = create_element(element["class"], element_x, element_y, element_height, element_width)
            screen.append( element_svg )

            if element["class"] not in components_array:
                components_array.append( element["class"] )

            # print("New element " + element["class"] + ":")
            # print("   Offset: " + str(element_offset["x"]) + ":" + str(element_offset["y"]))
            # print("   Position: " + str(element_x) + ":" + str(element_y))
            # print("   Size: " + str(element["height"]) + ":" + str(element["width"]))

        # Save Screen
        page_name = empty_project_id[0:- len(str(count)) ] + str(count)
        count += 1
        screen.save( folder_path + "/final/" + page_name  + ".svg" )
        files_name_array[file_name] = page_name


empty_project_id = "c29b5282-da70-8012-8003-70a99a4124a2"

def build_project(dir):
    final_dir = dir + "/final/"
    shutil.copytree( APP_ROOT + "/empty/", final_dir + "project/" )
    for file in os.listdir( final_dir ):
        if file.endswith(".svg"):
            shutil.move( final_dir + file, final_dir + "project/" + empty_project_id )
    
    
def compact_project(dir, project):
    project_dir = dir + "/final/project/"
    project_path = dir + "/final/" + project
    with zipfile.ZipFile(project_path + ".zip", "w") as zip_file:
        dir_files = os.listdir( project_dir )
        for file in dir_files:
            zip_file.write( project_dir + file, file )
        
        dir_files = os.listdir( project_dir + empty_project_id  )
        for file in dir_files:
            zip_file.write( project_dir + empty_project_id + "/" + file, empty_project_id + "/" + file )


def build_manifest(dir, project ):

    manifest_json_str = dir + "/final/project/manifest.json"
    manifest_json = json.load( open(manifest_json_str, "r") )

    for file in files_name_array:
        print(file)
        manifest_json["files"][empty_project_id]["pagesIndex"][files_name_array[file]] = {"name" : file} #.insert( , file )
        manifest_json["files"][empty_project_id]["pages"].append(files_name_array[file])
    manifest_json["files"][empty_project_id]["name"] = project

    json.dump( manifest_json, open( manifest_json_str, "w") )
    asd = 0


def detect(projectPath, sketchCode):

    print(APP_ROOT)
    print(projectPath)
    print(sketchCode)

    predict_folder( projectPath )

    build_components( projectPath )

    build_project( projectPath )

    build_manifest( projectPath, sketchCode )

    compact_project( projectPath, sketchCode)
