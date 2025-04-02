# -*- coding: utf-8 -*-
#__author__ = "Mohammad Sajjad Mortazavi"
# root.py

import os
#Mother root
def pathname():
    script_path = os.path.realpath(__file__)
    folder_name = 'BIM-Pars.tab'   
    folder_index = script_path.lower().find(folder_name.lower())
    if folder_index != -1:
        script_path_until_folder = script_path[:folder_index + len(folder_name)]
        return script_path_until_folder
    else:
        raise ValueError('Folder name "{}" not found in the script path.'.format(folder_name))
#API
def settings():
    script_path_until_folder = pathname()
    settings = os.path.join(script_path_until_folder, 'data','set','settings.xml')
    return settings

def app_strings():
    script_path_until_folder = pathname()
    app_string = os.path.join(script_path_until_folder, 'data','set','app_strings.json')
    return app_string

#APP
def app_logo_icon():
    script_path_until_folder = pathname()
    app_logo_icon = os.path.join(script_path_until_folder, 'data','pars_app','pars_logo_icon_red.ico')
    return app_logo_icon

def app_logo_name_icon():
    script_path_until_folder = pathname()
    app_logo_name_icon = os.path.join(script_path_until_folder, 'data','logo','name1.png')
    return app_logo_name_icon

def run_directory_icon():
    script_path_until_folder = pathname()
    run_directory_icon = os.path.join(script_path_until_folder, 'data','pars_app','run_directory.png')
    return run_directory_icon

def toolbox_icon():
    script_path_until_folder = pathname()
    toolbox_icon = os.path.join(script_path_until_folder, 'data','pars_app','toolbox.png')
    return toolbox_icon
   
def bimparstools_icon():
    script_path_until_folder = pathname()
    bimparstools_icon = os.path.join(script_path_until_folder, 'data','pars_app','bimparstools.png')
    return bimparstools_icon

def report_icon():
    script_path_until_folder = pathname()
    report_icon = os.path.join(script_path_until_folder, 'data','pars_app','report.png')
    return report_icon

def settings_icon():
    script_path_until_folder = pathname()
    settings_icon = os.path.join(script_path_until_folder, 'data','pars_app','settings.png')
    return settings_icon

def select_icon():
    script_path_until_folder = pathname()
    select_icon = os.path.join(script_path_until_folder, 'data','pars_app','select.png')
    return select_icon

def tool_icon():
    script_path_until_folder = pathname()
    tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tool.png')
    return tool_icon

def python_icon():
    script_path_until_folder = pathname()
    python_icon = os.path.join(script_path_until_folder, 'data','pars_app','python.png')
    return python_icon

def info_icon():
    script_path_until_folder = pathname()
    info_icon = os.path.join(script_path_until_folder, 'data','pars_app','info.png')
    return info_icon

def element_self_icon():
    script_path_until_folder = pathname()
    element_self_icon = os.path.join(script_path_until_folder, 'data','pars_app','element_self.png')
    return element_self_icon

def element_parameter_icon():
    script_path_until_folder = pathname()
    element_parameter_icon = os.path.join(script_path_until_folder, 'data','pars_app','element_parameter.png')
    return element_parameter_icon

def select_elements_icon():
    script_path_until_folder = pathname()
    select_elements_icon = os.path.join(script_path_until_folder, 'data','pars_app','select_elements.png')
    return select_elements_icon

def reduce_selected_elements_icon():
    script_path_until_folder = pathname()
    reduce_selected_elements_icon = os.path.join(script_path_until_folder, 'data','pars_app','reduce_selected_elements.png')
    return reduce_selected_elements_icon

def delete_app_icon():
    script_path_until_folder = pathname()
    delete_app_icon = os.path.join(script_path_until_folder, 'data','pars_app','delete.png')
    return delete_app_icon

def parameter_self_icon():
    script_path_until_folder = pathname()
    parameter_self_icon = os.path.join(script_path_until_folder, 'data','pars_app','parameter_self.png')
    return parameter_self_icon

def parameter_value_icon():
    script_path_until_folder = pathname()
    parameter_value_icon = os.path.join(script_path_until_folder, 'data','pars_app','parameter_value.png')
    return parameter_value_icon

def filter_node_icon():
    script_path_until_folder = pathname()
    filter_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','filter_node.png')
    return filter_node_icon

def by_parameter_node_icon():
    script_path_until_folder = pathname()
    by_parameter_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','by_parameter_node.png')
    return by_parameter_node_icon

def all_elements_node_icon():
    script_path_until_folder = pathname()
    all_elements_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','all_elements_node.png')
    return all_elements_node_icon

def excel_node_icon():
    script_path_until_folder = pathname()
    excel_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','excel_node.png')
    return excel_node_icon

def search_node_icon():
    script_path_until_folder = pathname()
    search_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','search_node.png')
    return search_node_icon

def check_node_icon():
    script_path_until_folder = pathname()
    check_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','check_node.png')
    return check_node_icon

def delete_node_icon():
    script_path_until_folder = pathname()
    delete_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','delete_node.png')
    return delete_node_icon

def search_param_node_icon():
    script_path_until_folder = pathname()
    search_param_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','search_param_node.png')
    return search_param_node_icon

def compare_check_node_icon():
    script_path_until_folder = pathname()
    compare_check_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','compare_check_node.png')
    return compare_check_node_icon

def set_node_icon():
    script_path_until_folder = pathname()
    set_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','set_node.png')
    return set_node_icon

def edit_node_icon():
    script_path_until_folder = pathname()
    edit_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','edit_node.png')
    return edit_node_icon

def delete_param_node_icon():
    script_path_until_folder = pathname()
    delete_param_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','delete_param_node.png')
    return delete_param_node_icon

def folder_icon():
    script_path_until_folder = pathname()
    folder_icon = os.path.join(script_path_until_folder, 'data','pars_app','folder.png')
    return folder_icon

def lab_user_node_icon():
    script_path_until_folder = pathname()
    lab_user_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','lab_user_node.png')
    return lab_user_node_icon

def expand_tree_button():
    script_path_until_folder = pathname()
    expand_tree_button = os.path.join(script_path_until_folder, 'data','pars_app','expand_tree.png')
    return expand_tree_button

def expand_tree_button():
    script_path_until_folder = pathname()
    expand_tree_button = os.path.join(script_path_until_folder, 'data','pars_app','expand_tree.png')
    return expand_tree_button
##
def close_tree_button():
    script_path_until_folder = pathname()
    close_tree_button = os.path.join(script_path_until_folder, 'data','pars_app','close_tree.png')
    return close_tree_button

def user_manual_button():
    script_path_until_folder = pathname()
    user_manual_button = os.path.join(script_path_until_folder, 'data','pars_app','user_manual.png')
    return user_manual_button

def video_youtube_button():
    script_path_until_folder = pathname()
    video_youtube_button= os.path.join(script_path_until_folder, 'data','pars_app','video.png')
    return video_youtube_button

def github_button():
    script_path_until_folder = pathname()
    github_button= os.path.join(script_path_until_folder, 'data','pars_app','github.png')
    return github_button

def report_bug_button():
    script_path_until_folder = pathname()
    report_bug_button = os.path.join(script_path_until_folder, 'data','pars_app','report_bug.png')
    return report_bug_button

def local_memory_in_button():
    script_path_until_folder = pathname()
    local_memory_in_button = os.path.join(script_path_until_folder, 'data','pars_app','local_memory_in.png')
    return local_memory_in_button

def local_memory_out_button():
    script_path_until_folder = pathname()
    local_memory_out_button = os.path.join(script_path_until_folder, 'data','pars_app','local_memory_out.png')
    return local_memory_out_button

def save_app_button():
    script_path_until_folder = pathname()
    save_app_button = os.path.join(script_path_until_folder, 'data','pars_app','save_app.png')
    return save_app_button

def download_app_button():
    script_path_until_folder = pathname()
    download_app_button = os.path.join(script_path_until_folder, 'data','pars_app','download_app.png')
    return download_app_button

def import_app_button():
    script_path_until_folder = pathname()
    import_app_button = os.path.join(script_path_until_folder, 'data','pars_app','import_app.png')
    return import_app_button

def export_app_button():
    script_path_until_folder = pathname()
    export_app_button = os.path.join(script_path_until_folder, 'data','pars_app','export_app.png')
    return export_app_button

def xml_app_button():
    script_path_until_folder = pathname()
    xml_app_button = os.path.join(script_path_until_folder, 'data','pars_app','xml.png')
    return xml_app_button

def html_app_button():
    script_path_until_folder = pathname()
    html_app_button = os.path.join(script_path_until_folder, 'data','pars_app','html.png')
    return html_app_button

def csv_app_button():
    script_path_until_folder = pathname()
    csv_app_button = os.path.join(script_path_until_folder, 'data','pars_app','csv.png')
    return csv_app_button

def deselect_elements_button():
    script_path_until_folder = pathname()
    deselect_elements_button = os.path.join(script_path_until_folder, 'data','pars_app','deselect_elements.png')
    return deselect_elements_button

def isolate_elements_button():
    script_path_until_folder = pathname()
    isolate_elements_button = os.path.join(script_path_until_folder, 'data','pars_app','isolate_elements.png')
    return isolate_elements_button

def deisolate_elements_button():
    script_path_until_folder = pathname()
    deisolate_elements_button = os.path.join(script_path_until_folder, 'data','pars_app','deisolate_elements.png')
    return deisolate_elements_button

def color_elements_button():
    script_path_until_folder = pathname()
    color_elements_button = os.path.join(script_path_until_folder, 'data','pars_app','color_elements.png')
    return color_elements_button

def decolor_elements_button():
    script_path_until_folder = pathname()
    decolor_elements_button = os.path.join(script_path_until_folder, 'data','pars_app','decolor_elements.png')
    return decolor_elements_button

def pin_button():
    script_path_until_folder = pathname()
    pin_button = os.path.join(script_path_until_folder, 'data','pars_app','pin.png')
    return pin_button

def unpin_button():
    script_path_until_folder = pathname()
    unpin_button = os.path.join(script_path_until_folder, 'data','pars_app','unpin.png')
    return unpin_button

def element_count_app_icon():
    script_path_until_folder = pathname()
    element_count_app_icon = os.path.join(script_path_until_folder, 'data','pars_app','element_count.png')
    return element_count_app_icon

def loading_connection_app_icon():
    script_path_until_folder = pathname()
    loading_connection_app_icon = os.path.join(script_path_until_folder, 'data','pars_app','loading_connection.png')
    return loading_connection_app_icon

def loading_user_app_icon():
    script_path_until_folder = pathname()
    loading_user_app_icon = os.path.join(script_path_until_folder, 'data','pars_app','loading_user.png')
    return loading_user_app_icon

def pyrevit_icon():
    script_path_until_folder = pathname()
    pyrevit_icon = os.path.join(script_path_until_folder, 'data','pars_app','pyrevit.png')
    return pyrevit_icon

def python_script_node_icon():
    script_path_until_folder = pathname()
    python_script_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','python_script.png')
    return python_script_node_icon

def back_tab_button():
    script_path_until_folder = pathname()
    back_tab_button = os.path.join(script_path_until_folder, 'data','pars_app','back_tab.png')
    return back_tab_button

def print_app_report_button():
    script_path_until_folder = pathname()
    print_app_report_button = os.path.join(script_path_until_folder, 'data','pars_app','print_app_report.png')
    return print_app_report_button

def clean_button():
    script_path_until_folder = pathname()
    clean_button = os.path.join(script_path_until_folder, 'data','pars_app','clean.png')
    return clean_button

def xlsx_app_button():
    script_path_until_folder = pathname()
    xlsx_app_button = os.path.join(script_path_until_folder, 'data','pars_app','xlsx.png')
    return xlsx_app_button

def filter_app_button():
    script_path_until_folder = pathname()
    filter_app_button = os.path.join(script_path_until_folder, 'data','pars_app','filter_app.png')
    return filter_app_button

def find_app_button():
    script_path_until_folder = pathname()
    find_app_button = os.path.join(script_path_until_folder, 'data','pars_app','find_app.png')
    return find_app_button

def edit_app_button():
    script_path_until_folder = pathname()
    edit_app_button = os.path.join(script_path_until_folder, 'data','pars_app','edit_app.png')
    return edit_app_button

def color_app_button():
    script_path_until_folder = pathname()
    color_app_button = os.path.join(script_path_until_folder, 'data','pars_app','color.png')
    return color_app_button

def add_bottom_app_button():
    script_path_until_folder = pathname()
    add_bottom_app_button = os.path.join(script_path_until_folder, 'data','pars_app','add_bottom.png')
    return add_bottom_app_button

def add_top_app_button():
    script_path_until_folder = pathname()
    add_top_app_button = os.path.join(script_path_until_folder, 'data','pars_app','add_top.png')
    return add_top_app_button

def add_right_app_button():
    script_path_until_folder = pathname()
    add_right_app_button = os.path.join(script_path_until_folder, 'data','pars_app','add_right.png')
    return add_right_app_button

def add_left_app_button():
    script_path_until_folder = pathname()
    add_left_app_button = os.path.join(script_path_until_folder, 'data','pars_app','add_left.png')
    return add_left_app_button

def write_app_button():
    script_path_until_folder = pathname()
    write_app_button = os.path.join(script_path_until_folder, 'data','pars_app','write.png')
    return write_app_button

def delete_row_app_button():
    script_path_until_folder = pathname()
    delete_row_app_button = os.path.join(script_path_until_folder, 'data','pars_app','delete_row.png')
    return delete_row_app_button

def delete_column_app_button():
    script_path_until_folder = pathname()
    delete_column_app_button = os.path.join(script_path_until_folder, 'data','pars_app','delete_column.png')
    return delete_column_app_button

def delete_hiden_app_button():
    script_path_until_folder = pathname()
    delete_hiden_app_button = os.path.join(script_path_until_folder, 'data','pars_app','delete_hiden.png')
    return delete_hiden_app_button

def similar_item_color_button():
    script_path_until_folder = pathname()
    similar_item_color_button = os.path.join(script_path_until_folder, 'data','pars_app','similar_item_color.png')
    return similar_item_color_button

def similar_item_color_full_sheet_button():
    script_path_until_folder = pathname()
    similar_item_color_full_sheet_button = os.path.join(script_path_until_folder, 'data','pars_app','similar_item_color_full_sheet.png')
    return similar_item_color_full_sheet_button

def numeric_gradient_button():
    script_path_until_folder = pathname()
    numeric_gradient_button = os.path.join(script_path_until_folder, 'data','pars_app','numeric_gradient.png')
    return numeric_gradient_button

def paint_app_button():
    script_path_until_folder = pathname()
    paint_app_button = os.path.join(script_path_until_folder, 'data','pars_app','paint_app.png')
    return paint_app_button

def bimpars_report_icon():
    script_path_until_folder = pathname()
    bimpars_report_icon = os.path.join(script_path_until_folder, 'data','pars_app','bimpars_report.png')
    return bimpars_report_icon

def user_app_icon():
    script_path_until_folder = pathname()
    user_app_icon = os.path.join(script_path_until_folder, 'data','pars_app','user.png')
    return user_app_icon

def valid_user_app_icon():
    script_path_until_folder = pathname()
    valid_user_app_icon = os.path.join(script_path_until_folder, 'data','pars_app','valid_user.png')
    return valid_user_app_icon

def unvalid_user_app_icon():
    script_path_until_folder = pathname()
    unvalid_user_app_icon = os.path.join(script_path_until_folder, 'data','pars_app','unvalid_user.png')
    return unvalid_user_app_icon

def online_app_icon():
    script_path_until_folder = pathname()
    online_app_icon = os.path.join(script_path_until_folder, 'data','pars_app','online.png')
    return online_app_icon

def offline_app_icon():
    script_path_until_folder = pathname()
    offline_app_icon = os.path.join(script_path_until_folder, 'data','pars_app','offline.png')
    return offline_app_icon

def find_app_ico_icon():
    script_path_until_folder = pathname()
    find_app_ico_icon = os.path.join(script_path_until_folder, 'data','pars_app','find_app.ico')
    return find_app_ico_icon

def find_app_gif_icon():
    script_path_until_folder = pathname()
    find_app_ico_icon = os.path.join(script_path_until_folder, 'data','pars_app','find_app.gif')
    return find_app_ico_icon

def write_app_ico_icon():
    script_path_until_folder = pathname()
    write_app_ico_icon = os.path.join(script_path_until_folder, 'data','pars_app','write.ico')
    return write_app_ico_icon

#APP TOOLS ICONS
def element_id_app_tool_icon():
    script_path_until_folder = pathname()
    element_id_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','element_id.png')
    return element_id_app_tool_icon

def creator_finder_app_tool_icon():
    script_path_until_folder = pathname()
    creator_finder_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','creator_finder.png')
    return creator_finder_app_tool_icon

def information_app_tool_icon():
    script_path_until_folder = pathname()
    information_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','information.png')
    return information_app_tool_icon

def active_view_app_tool_icon():
    script_path_until_folder = pathname()
    active_view_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','active_view.png')
    return active_view_app_tool_icon

def hierarchy_app_tool_icon():
    script_path_until_folder = pathname()
    hierarchy_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','hierarchy.png')
    return hierarchy_app_tool_icon

def dudul_app_tool_icon():
    script_path_until_folder = pathname()
    dudul_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','dudul.png')
    return dudul_app_tool_icon

def by_type_app_tool_icon():
    script_path_until_folder = pathname()
    by_type_filter_select_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','by_type.png')
    return by_type_filter_select_app_tool_icon

def search_for_value_of_instance_parameters_app_tool_icon():
    script_path_until_folder = pathname()
    search_for_value_of_instance_parameters_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','search_for_value_of_instance_parameters.png')
    return search_for_value_of_instance_parameters_app_tool_icon

def existance_of_parameters_values_app_tool_icon():
    script_path_until_folder = pathname()
    existance_of_parameters_values_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','existance_of_parameters_values.png')
    return existance_of_parameters_values_app_tool_icon

def all_elements_in_selected_categories_app_tool_icon():
    script_path_until_folder = pathname()
    all_elements_in_selected_categories_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','all_elements_in_selected_categories.png')
    return all_elements_in_selected_categories_app_tool_icon

def all_elements_in_selected_views_app_tool_icon():
    script_path_until_folder = pathname()
    all_elements_in_selected_views_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','all_elements_in_selected_views.png')
    return all_elements_in_selected_views_app_tool_icon

def all_elements_of_selected_levels_app_tool_icon():
    script_path_until_folder = pathname()
    all_elements_of_selected_levels_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','all_elements_of_selected_levels.png')
    return all_elements_of_selected_levels_app_tool_icon

def ownership_of_elements_app_tool_icon():
    script_path_until_folder = pathname()
    ownership_of_elements_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','ownership_of_elements.png')
    return ownership_of_elements_app_tool_icon

def unbound_rooms_app_tool_icon():
    script_path_until_folder = pathname()
    unbound_rooms_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','unbound_rooms.png')
    return unbound_rooms_app_tool_icon

def mirrored_doors_app_tool_icon():
    script_path_until_folder = pathname()
    mirrored_doors_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','mirrored_doors.png')
    return mirrored_doors_app_tool_icon

def ids_from_excel_app_tool_icon():
    script_path_until_folder = pathname()
    ids_from_excel_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','ids_from_excel.png')
    return ids_from_excel_app_tool_icon

def by_id_app_tool_icon():
    script_path_until_folder = pathname()
    by_id_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','by_id.png')
    return by_id_app_tool_icon

def all_direct_shape_elements_app_tool_icon():
    script_path_until_folder = pathname()
    all_direct_shape_elements_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','all_direct_shape_elements.png')
    return all_direct_shape_elements_app_tool_icon

def search_value_of_parameters_by_filter_app_tool_icon():
    script_path_until_folder = pathname()
    search_value_of_parameters_by_filter_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','search_value_of_parameters_by_filter.png')
    return search_value_of_parameters_by_filter_app_tool_icon

def search_value_of_parameters_by_filter_for_family_document_app_tool_icon():
    script_path_until_folder = pathname()
    search_value_of_parameters_by_filter_for_family_document_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','search_value_of_parameters_by_filter_for_family_document.png')
    return search_value_of_parameters_by_filter_for_family_document_app_tool_icon

def snipe_parameter_value_app_tool_icon():
    script_path_until_folder = pathname()
    snipe_parameter_value_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','snipe_parameter_value.png')
    return snipe_parameter_value_app_tool_icon

def snipe_parameter_value_for_family_document_app_tool_icon():
    script_path_until_folder = pathname()
    snipe_parameter_value_for_family_document_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','snipe_parameter_value_for_family_document.png')
    return snipe_parameter_value_for_family_document_app_tool_icon

def element_dictionary_app_tool_icon():
    script_path_until_folder = pathname()
    element_dictionary_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','element_dictionary.png')
    return element_dictionary_app_tool_icon

def check_parameter_against_category_app_tool_icon():
    script_path_until_folder = pathname()
    check_parameter_against_category_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','check_parameter_against_category.png')
    return check_parameter_against_category_app_tool_icon

def delete_parameter_completely_from_the_model_app_tool_icon():
    script_path_until_folder = pathname()
    delete_parameter_completely_from_the_model_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','delete_parameter_completely_from_the_model.png')
    return delete_parameter_completely_from_the_model_app_tool_icon

def search_for_any_value_app_tool_icon():
    script_path_until_folder = pathname()
    search_for_any_value_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','search_for_any_value.png')
    return search_for_any_value_app_tool_icon

def pair_comparer_app_tool_icon():
    script_path_until_folder = pathname()
    pair_comparer_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','pair_comparer.png')
    return pair_comparer_app_tool_icon

def comparer_of_multiple_elements_app_tool_icon():
    script_path_until_folder = pathname()
    comparer_of_multiple_elements_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','comparer_of_multiple_elements.png')
    return comparer_of_multiple_elements_app_tool_icon

def same_value_for_all_selected_elements_app_tool_icon():
    script_path_until_folder = pathname()
    same_value_for_all_selected_elements_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','same_value_for_all_selected_elements.png')
    return same_value_for_all_selected_elements_app_tool_icon

def copy_from_one_parameter_to_another_parameter_app_tool_icon():
    script_path_until_folder = pathname()
    copy_from_one_parameter_to_another_parameter_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','copy_from_one_parameter_to_another_parameter.png')
    return copy_from_one_parameter_to_another_parameter_app_tool_icon

def list_makers_of_values_from_excel_app_tool_icon():
    script_path_until_folder = pathname()
    list_makers_of_values_from_excel_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','list_makers_of_values_from_excel.png')
    return list_makers_of_values_from_excel_app_tool_icon

def batch_parameter_set_using_dataset_app_tool_icon():
    script_path_until_folder = pathname()
    batch_parameter_set_using_dataset_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','batch_parameter_set_using_dataset.png')
    return batch_parameter_set_using_dataset_app_tool_icon

def id_generator_app_tool_icon():
    script_path_until_folder = pathname()
    id_generator_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','id_generator.png')
    return id_generator_app_tool_icon

def parameter_value_editor_app_tool_icon():
    script_path_until_folder = pathname()
    parameter_value_editor_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','parameter_value_editor.png')
    return parameter_value_editor_app_tool_icon

def parameter_value_editor_for_special_characters_app_tool_icon():
    script_path_until_folder = pathname()
    parameter_value_editor_for_special_characters_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','parameter_value_editor_for_special_characters.png')
    return parameter_value_editor_for_special_characters_app_tool_icon

def value_of_parameter_for_selected_elements_app_tool_icon():
    script_path_until_folder = pathname()
    value_of_parameter_for_selected_elements_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','value_of_parameter_for_selected_elements.png')
    return value_of_parameter_for_selected_elements_app_tool_icon

def desired_character_in_value_of_parameter_for_selected_elements_app_tool_icon():
    script_path_until_folder = pathname()
    desired_character_in_value_of_parameter_for_selected_elements_app_tool_icon = os.path.join(script_path_until_folder, 'data','pars_app','tools','desired_character_in_value_of_parameter_for_selected_elements.png')
    return desired_character_in_value_of_parameter_for_selected_elements_app_tool_icon

def add_key_icon():
    script_path_until_folder = pathname()
    add_key_icon = os.path.join(script_path_until_folder, 'data','pars_app','add_key.png')
    return add_key_icon

def lock_ico_icon():
    script_path_until_folder = pathname()
    lock_ico_icon = os.path.join(script_path_until_folder, 'data','pars_app','lock_ico_icon.ico')
    return lock_ico_icon

def lock_gif_icon():
    script_path_until_folder = pathname()
    lock_gif_icon = os.path.join(script_path_until_folder, 'data','pars_app','lock_gif_icon.gif')
    return lock_gif_icon

def scripts_node_icon():
    script_path_until_folder = pathname()
    scripts_node_icon = os.path.join(script_path_until_folder, 'data','pars_app','scripts_node.png')
    return scripts_node_icon

#General
def logo_path():
    script_path_until_folder = pathname()
    logo_path = os.path.join(script_path_until_folder, 'data', 'logo.png')
    return logo_path

def cuslogo_path():
    script_path_until_folder = pathname()
    cuslogo_path = os.path.join(script_path_until_folder, 'data', 'cuslogo.png')
    return cuslogo_path

def lan_path():
    script_path_until_folder = pathname()
    lan_path = os.path.join(script_path_until_folder, 'data','set', 'lan.txt')
    return lan_path

def mod_path():
    script_path_until_folder = pathname()
    mod_path = os.path.join(script_path_until_folder, 'data','set', 'mod.txt')
    return mod_path

def key_path():
    script_path_until_folder = pathname()
    key_path = os.path.join(script_path_until_folder, 'data','set', 'key.json')
    return key_path

def update_path():
    script_path_until_folder = pathname()
    update_path = os.path.join(script_path_until_folder, 'data', 'update')
    return update_path

def storage_path():
    script_path_until_folder = pathname()
    storage_path = os.path.join(script_path_until_folder, 'data', 'storage')
    return storage_path

def pylist_path():
    script_path_until_folder = pathname()
    pylist_path = os.path.join(script_path_until_folder, 'data', 'pylist')
    return pylist_path

def loadlist():
    script_path_until_folder = pathname()
    loadlist = os.path.join(script_path_until_folder, 'data','loadlist')
    return loadlist

def wurl_path():
    script_path_until_folder = pathname()
    wurl_path = os.path.join(script_path_until_folder, 'data','set', 'wurl.txt')
    return wurl_path

def general_urls():
    script_path_until_folder = pathname()
    general_urls = os.path.join(script_path_until_folder, 'data','set')
    return general_urls

def exlist_path():
    script_path_until_folder = pathname()
    exlist_path = os.path.join(script_path_until_folder, 'data','exlist')
    return exlist_path

#Buttons
def ok_icon():
    script_path_until_folder = pathname()
    ok_icon = os.path.join(script_path_until_folder, 'data','buttons', 'ok.ico')
    return ok_icon

def cancel_icon():
    script_path_until_folder = pathname()
    cancel_icon = os.path.join(script_path_until_folder, 'data','buttons', 'cancel.ico')
    return cancel_icon

def print_icon():
    script_path_until_folder = pathname()
    print_icon = os.path.join(script_path_until_folder, 'data','buttons', 'print.ico')
    return print_icon

def comment_icon():
    script_path_until_folder = pathname()
    comment_icon = os.path.join(script_path_until_folder, 'data','ico', 'comment.ico')
    return comment_icon

def eye_icon():
    script_path_until_folder = pathname()
    eye_icon = os.path.join(script_path_until_folder, 'data','buttons', 'check.ico')
    return eye_icon

def submit_icon():
    script_path_until_folder = pathname()
    submit_icon = os.path.join(script_path_until_folder, 'data','buttons', 'submit.ico')
    return submit_icon

def compare_icon():
    script_path_until_folder = pathname()
    compare_icon = os.path.join(script_path_until_folder, 'data','buttons', 'compare.ico')
    return compare_icon

def right_button():
    script_path_until_folder = pathname()
    right_button = os.path.join(script_path_until_folder, 'data','buttons','right.ico')
    return right_button

def left_button():
    script_path_until_folder = pathname()
    left_button = os.path.join(script_path_until_folder, 'data','buttons','left.ico')
    return left_button

def filter_button():
    script_path_until_folder = pathname()
    filter_button = os.path.join(script_path_until_folder, 'data','buttons','filter.ico')
    return filter_button

def zoomextend_button():
    script_path_until_folder = pathname()
    zoomextend_button = os.path.join(script_path_until_folder, 'data','buttons','zoomextend.ico')
    return zoomextend_button

def walk_button():
    script_path_until_folder = pathname()
    walk_button = os.path.join(script_path_until_folder, 'data','buttons', 'walk.ico')
    return walk_button

def level_button():
    script_path_until_folder = pathname()
    level_button = os.path.join(script_path_until_folder, 'data','buttons', 'level.ico')
    return level_button

def levelview_button():
    script_path_until_folder = pathname()
    levelview_button = os.path.join(script_path_until_folder, 'data','buttons', 'levelview.ico')
    return levelview_button

def own_button():
    script_path_until_folder = pathname()
    own_button = os.path.join(script_path_until_folder, 'data','buttons', 'person.ico')
    return own_button

def xpown_button():
    script_path_until_folder = pathname()
    xpown_button = os.path.join(script_path_until_folder, 'data','buttons', 'xperson.ico')
    return xpown_button

def comment_button():
    script_path_until_folder = pathname()
    comment_button = os.path.join(script_path_until_folder, 'data','buttons', 'comment.ico')
    return comment_button

def importexc_button():
    script_path_until_folder = pathname()
    importexc_button = os.path.join(script_path_until_folder, 'data','buttons', 'import1.ico')
    return importexc_button

def importfile_button():
    script_path_until_folder = pathname()
    importfile_button = os.path.join(script_path_until_folder, 'data','buttons', 'import1.ico')
    return importfile_button

def export_button():
    script_path_until_folder = pathname()
    export_button = os.path.join(script_path_until_folder, 'data','buttons','export.ico')
    return export_button

def find_button():
    script_path_until_folder = pathname()
    find_button = os.path.join(script_path_until_folder, 'data','buttons', 'find.ico')
    return find_button

def deposit_button():
    script_path_until_folder = pathname()
    deposit_button = os.path.join(script_path_until_folder, 'data','buttons', 'deposit.ico')
    return deposit_button

def plus_button():
    script_path_until_folder = pathname()
    plus_button = os.path.join(script_path_until_folder, 'data','buttons', 'plus.ico')
    return plus_button

def minus_button():
    script_path_until_folder = pathname()
    minus_button = os.path.join(script_path_until_folder, 'data','buttons', 'minus.ico')
    return minus_button

def reset_icon():
    script_path_until_folder = pathname()
    reset_icon = os.path.join(script_path_until_folder, 'data','buttons', 'reset.ico')
    return reset_icon

def delete_row_button():
    script_path_until_folder = pathname()
    delete_row_button = os.path.join(script_path_until_folder, 'data','buttons', 'del_row.ico')
    return delete_row_button

def focus_button():
    script_path_until_folder = pathname()
    focus_button = os.path.join(script_path_until_folder, 'data','buttons', 'focus.ico')
    return focus_button

def save_button():
    script_path_until_folder = pathname()
    save_button = os.path.join(script_path_until_folder, 'data','buttons', 'save.ico')
    return save_button

def refresh_button():
    script_path_until_folder = pathname()
    refresh_button = os.path.join(script_path_until_folder, 'data','buttons', 'refresh.ico')
    return refresh_button

def filter2_button():
    script_path_until_folder = pathname()
    filter2_button = os.path.join(script_path_until_folder, 'data','buttons', 'filter_button.ico')
    return filter2_button

#Element ID
def commentgif():
    script_path_until_folder = pathname()
    commentgif = os.path.join(script_path_until_folder, 'data','gif', 'comment4.gif')
    return commentgif

def icon_SelectGtID():
    script_path_until_folder = pathname()
    icon_SelectGtID = os.path.join(script_path_until_folder, 'data','ico', 'SelectGetID.ico')
    return icon_SelectGtID

#Information
def infoch_icon():
    script_path_until_folder = pathname()
    infoch_icon = os.path.join(script_path_until_folder, 'data','ico', 'info.ico')
    return infoch_icon

def infoch_cskin():
    script_path_until_folder = pathname()
    infoch_cskin = os.path.join(script_path_until_folder, 'data','gif', 'cool_info.gif')
    return infoch_cskin

def infoch_bskin():
    script_path_until_folder = pathname()
    infoch_bskin = os.path.join(script_path_until_folder, 'data','gif', 'info.gif')
    return infoch_bskin

def minfo_sym():
    script_path_until_folder = pathname()
    minfo_sym = os.path.join(script_path_until_folder, 'data','sym', 'MInfo.png')
    return minfo_sym

def pinfo_sym():
    script_path_until_folder = pathname()
    pinfo_sym = os.path.join(script_path_until_folder, 'data','sym', 'PInfo.png')
    return pinfo_sym

def cinfo_sym():
    script_path_until_folder = pathname()
    cinfo_sym = os.path.join(script_path_until_folder, 'data','sym', 'Category.png')
    return cinfo_sym

def finfo_sym():
    script_path_until_folder = pathname()
    finfo_sym = os.path.join(script_path_until_folder, 'data','sym', 'FamilyTree.png')
    return finfo_sym

def camodel_sym():
    script_path_until_folder = pathname()
    camodel_sym = os.path.join(script_path_until_folder, 'data','sym', 'CaInModel.png')
    return camodel_sym

def caview_sym():
    script_path_until_folder = pathname()
    camodel_sym = os.path.join(script_path_until_folder, 'data','sym', 'CaInView.png')
    return camodel_sym

def xml_sym():
    script_path_until_folder = pathname()
    xml_sym = os.path.join(script_path_until_folder, 'data','sym', 'xml.png')
    return xml_sym

#Creator Finder
def creator_icon():
    script_path_until_folder = pathname()
    creator_icon = os.path.join(script_path_until_folder, 'data','ico', 'creator.ico')
    return creator_icon

#Search value of parameter by filter
def pvaluefilter_icon():
    script_path_until_folder = pathname()
    pvaluefilter_icon = os.path.join(script_path_until_folder, 'data','ico', 'pvaluebyfilter.ico')
    return pvaluefilter_icon

#Existance of parameters values
def pvalue_back():
    script_path_until_folder = pathname()
    creator_icon = os.path.join(script_path_until_folder, 'data','gif', 'PValueForExist.gif')
    return creator_icon

def pvalue_icon():
    script_path_until_folder = pathname()
    creator_icon = os.path.join(script_path_until_folder, 'data','ico', 'PValueForExist.ico')
    return creator_icon

def parameterexistance_icon():
    script_path_until_folder = pathname()
    parameterexistance_icon = os.path.join(script_path_until_folder, 'data','ico', 'parameterexistance.ico')
    return parameterexistance_icon

#Search for value of instance parameters
def sinstancepv_icon():
    script_path_until_folder = pathname()
    sinstancepv_icon = os.path.join(script_path_until_folder, 'data','ico', 'SearchForInstancePValue.ico')
    return sinstancepv_icon

def sinstancepv_back():
    script_path_until_folder = pathname()
    sinstancepv_back = os.path.join(script_path_until_folder, 'data','gif', 'SearchForInstancePValue.gif')
    return sinstancepv_back

def searchvalue_icon():
    script_path_until_folder = pathname()
    searchvalue_sym = os.path.join(script_path_until_folder, 'data','ico', 'searchvalue.ico')
    return searchvalue_sym

#Search for any value
def sanyv_icon():
    script_path_until_folder = pathname()
    sanyv_icon_icon = os.path.join(script_path_until_folder, 'data','ico', 'SearchForAnyValue.ico')
    return sanyv_icon_icon

def sanyv_back():
    script_path_until_folder = pathname()
    sanyv_back = os.path.join(script_path_until_folder, 'data','gif', 'searching.gif')
    return sanyv_back

def searchanyvalue_icon():
    script_path_until_folder = pathname()
    searchanyvalue_icon = os.path.join(script_path_until_folder, 'data','ico', 'searchanyvalue.ico')
    return searchanyvalue_icon

#Same value for all selected elements
def onevalue_icon():
    script_path_until_folder = pathname()
    onevalue_icon = os.path.join(script_path_until_folder, 'data','ico', 'onevalue.ico')
    return onevalue_icon

def onevalue_back():
    script_path_until_folder = pathname()
    onevalue_back = os.path.join(script_path_until_folder, 'data','gif', 'onevalue.gif')
    return onevalue_back

#Copy from one parameter to another parameter
def copy_icon():
    script_path_until_folder = pathname()
    copy_icon = os.path.join(script_path_until_folder, 'data','ico', 'copy.ico')
    return copy_icon

def copy_back():
    script_path_until_folder = pathname()
    copy_back = os.path.join(script_path_until_folder, 'data','gif', 'copy.gif')
    return copy_back

#List maker of values from Excel
def excel_list_icon():
    script_path_until_folder = pathname()
    excel_list_icon = os.path.join(script_path_until_folder, 'data','ico', 'excel_list.ico')
    return excel_list_icon

def excel_list_back():
    script_path_until_folder = pathname()
    excel_list_back = os.path.join(script_path_until_folder, 'data','gif', 'excel_list.png')
    return excel_list_back

def excel_list_sym():
    script_path_until_folder = pathname()
    excel_list_sym = os.path.join(script_path_until_folder, 'data','sym', 'excel_list.png')
    return excel_list_sym

#Parameter List based on Element ID
def param_tasklist_icon():
    script_path_until_folder = pathname()
    param_tasklist_icon = os.path.join(script_path_until_folder, 'data','ico', 'param_tasklist.ico')
    return param_tasklist_icon

def param_tasklist_back():
    script_path_until_folder = pathname()
    param_tasklist_back = os.path.join(script_path_until_folder, 'data','gif', 'param_tasklist.png')
    return param_tasklist_back

def param_tasklist_sym():
    script_path_until_folder = pathname()
    param_tasklist_sym = os.path.join(script_path_until_folder, 'data','sym', 'param_tasklist_sym.ico')
    return param_tasklist_sym

def save_tasklist_back():
    script_path_until_folder = pathname()
    save_tasklist_back = os.path.join(script_path_until_folder, 'data','gif', 'save_tasklist.png')
    return save_tasklist_back

def dataset_back():
    script_path_until_folder = pathname()
    dataset_back = os.path.join(script_path_until_folder, 'data','gif', 'dataset_back.png')
    return dataset_back
#Batch Parameter Set using Dataset
def param_tasklist_icon():
    script_path_until_folder = pathname()
    param_tasklist_icon = os.path.join(script_path_until_folder, 'data','ico', 'param_tasklist.ico')
    return param_tasklist_icon

def param_tasklist_back():
    script_path_until_folder = pathname()
    param_tasklist_back = os.path.join(script_path_until_folder, 'data','gif', 'param_tasklist.png')
    return param_tasklist_back

def param_tasklist_sym():
    script_path_until_folder = pathname()
    param_tasklist_sym = os.path.join(script_path_until_folder, 'data','sym', 'param_tasklist_sym.ico')
    return param_tasklist_sym

def save_tasklist_back():
    script_path_until_folder = pathname()
    save_tasklist_back = os.path.join(script_path_until_folder, 'data','gif', 'save_tasklist.png')
    return save_tasklist_back

def dataset_back():
    script_path_until_folder = pathname()
    dataset_back = os.path.join(script_path_until_folder, 'data','gif', 'dataset_back.png')
    return dataset_back

def category_list_back():
    script_path_until_folder = pathname()
    category_list_back = os.path.join(script_path_until_folder, 'data','gif', 'category_list_back.png')
    return category_list_back

def category_list_sym():
    script_path_until_folder = pathname()
    category_list_sym = os.path.join(script_path_until_folder, 'data','sym', 'category_list_sym.ico')
    return category_list_sym

def convert_file_back():
    script_path_until_folder = pathname()
    convert_file_back = os.path.join(script_path_until_folder, 'data','gif', 'convert_file.png')
    return convert_file_back

def convert_file_back2():
    script_path_until_folder = pathname()
    convert_file_back = os.path.join(script_path_until_folder, 'data','gif', 'convert_file_back.png')
    return convert_file_back

def convert_file_icon():
    script_path_until_folder = pathname()
    convert_file_icon = os.path.join(script_path_until_folder, 'data','ico', 'convert_file_icon.ico')
    return convert_file_icon

#Parameter value editor
def math_back():
    script_path_until_folder = pathname()
    math_back = os.path.join(script_path_until_folder, 'data','gif', 'mathoperation.gif')
    return math_back

def math_icon():
    script_path_until_folder = pathname()
    math_icon = os.path.join(script_path_until_folder, 'data','ico', 'math.ico')
    return math_icon

def ranstring_icon():
    script_path_until_folder = pathname()
    ranstring_icon = os.path.join(script_path_until_folder, 'data','ico', 'ranstring.ico')
    return ranstring_icon

def editor_icon():
    script_path_until_folder = pathname()
    editor_icon = os.path.join(script_path_until_folder, 'data','ico', 'PValueEditor.ico')
    return editor_icon

def editor_back():
    script_path_until_folder = pathname()
    editor_back = os.path.join(script_path_until_folder, 'data','gif', 'edit.gif')
    return editor_back

def replace_back():
    script_path_until_folder = pathname()
    replace_back = os.path.join(script_path_until_folder, 'data','gif', 'change.gif')
    return replace_back

def prefix_back():
    script_path_until_folder = pathname()
    prefix_back = os.path.join(script_path_until_folder, 'data','gif', 'left.gif')
    return prefix_back

def suffix_back():
    script_path_until_folder = pathname()
    suffix_back = os.path.join(script_path_until_folder, 'data','gif', 'right.gif')
    return suffix_back

def replace_sym():
    script_path_until_folder = pathname()
    replace_sym = os.path.join(script_path_until_folder, 'data','sym', 'replace.png')
    return replace_sym

def prefix_sym():
    script_path_until_folder = pathname()
    prefix_sym = os.path.join(script_path_until_folder, 'data','sym', 'prefix.png')
    return prefix_sym

def suffix_sym():
    script_path_until_folder = pathname()
    suffix_sym = os.path.join(script_path_until_folder, 'data','sym', 'suffix.png')
    return suffix_sym

#Parameter value editor for special characters
def comma_icon():
    script_path_until_folder = pathname()
    comma_icon = os.path.join(script_path_until_folder, 'data','ico', 'comma.ico')
    return comma_icon

def comma_back():
    script_path_until_folder = pathname()
    comma_back = os.path.join(script_path_until_folder, 'data','gif', 'comma.gif')
    return comma_back

def replace_back():
    script_path_until_folder = pathname()
    replace_back = os.path.join(script_path_until_folder, 'data','gif', 'change.gif')
    return replace_back

def borcomma_back():
    script_path_until_folder = pathname()
    borcomma_back = os.path.join(script_path_until_folder, 'data','gif', 'borcomma.png')
    return borcomma_back

#ID Generator
def borid_back():
    script_path_until_folder = pathname()
    borid_back = os.path.join(script_path_until_folder, 'data','gif', 'IDGenerator.png')
    return borid_back

def id_icon():
    script_path_until_folder = pathname()
    id_icon = os.path.join(script_path_until_folder, 'data','ico', 'id.ico')
    return id_icon

def id_back():
    script_path_until_folder = pathname()
    id_back = os.path.join(script_path_until_folder, 'data','gif', 'DNA.gif')
    return id_back

def searchbar_icon():
    script_path_until_folder = pathname()
    searchbar_icon = os.path.join(script_path_until_folder, 'data','ico', 'searchbar.ico')
    return searchbar_icon

def searchbar_back():
    script_path_until_folder = pathname()
    searchbar_back = os.path.join(script_path_until_folder, 'data','gif', 'count.gif')
    return searchbar_back

def rannumber_icon():
    script_path_until_folder = pathname()
    rannumber_icon = os.path.join(script_path_until_folder, 'data','ico', 'rannumber.ico')
    return rannumber_icon

def rannumber_back():
    script_path_until_folder = pathname()
    rannumber_back = os.path.join(script_path_until_folder, 'data','gif', 'number.gif')
    return rannumber_back

def ranstring_back():
    script_path_until_folder = pathname()
    ranstring_back = os.path.join(script_path_until_folder, 'data','gif', 'infinit.gif')
    return ranstring_back

#Pair comparer
def outcompare1():
    script_path_until_folder = pathname()
    outcompare1 = os.path.join(script_path_until_folder, 'data','ico', 'outcompare1.ico')
    return outcompare1

def two_sym():
    script_path_until_folder = pathname()
    two_sym = os.path.join(script_path_until_folder, 'data','sym', 'SelectTwoCompare.png')
    return two_sym

def comparev_back():
    script_path_until_folder = pathname()
    comparev_back = os.path.join(script_path_until_folder, 'data','gif', 'view.png')
    return comparev_back

def comparee_back():
    script_path_until_folder = pathname()
    comparee_back = os.path.join(script_path_until_folder, 'data','gif', 'element.png')
    return comparee_back

def comparetwo_icon():
    script_path_until_folder = pathname()
    comma_icon = os.path.join(script_path_until_folder, 'data','ico', 'judge.ico')
    return comma_icon

#Comparer of multiple elements
def multi_sym():
    script_path_until_folder = pathname()
    multi_sym = os.path.join(script_path_until_folder, 'data','sym', 'MultiCompare.png')
    return multi_sym

def outcompare2():
    script_path_until_folder = pathname()
    outcompare2 = os.path.join(script_path_until_folder, 'data','ico', 'outcompare2.ico')
    return outcompare2

#Snipe parameter value
def snipers_icon():
    script_path_until_folder = pathname()
    snipers_icon = os.path.join(script_path_until_folder, 'data','ico', 'snipers.ico')
    return snipers_icon

#Element Dictionary
def elementdict_icon():
    script_path_until_folder = pathname()
    elementdict_icon = os.path.join(script_path_until_folder, 'data','ico', 'dictionary.ico')
    return elementdict_icon

#Hierarchy
def hierchy_icon():
    script_path_until_folder = pathname()
    hierchy_icon = os.path.join(script_path_until_folder, 'data','ico','hierchy_icon.ico')
    return hierchy_icon

def borhierchy_back():
    script_path_until_folder = pathname()
    borhierchy_icon = os.path.join(script_path_until_folder, 'data','gif','hierchy_back.png')
    return borhierchy_icon

def coohierchy_back():
    script_path_until_folder = pathname()
    coohierchy_back = os.path.join(script_path_until_folder, 'data','gif','fh.gif')
    return coohierchy_back

def filter_icon():
    script_path_until_folder = pathname()
    filter_icon = os.path.join(script_path_until_folder, 'data','ico','filter.ico')
    return filter_icon

def filterparam_back():
    script_path_until_folder = pathname()
    filterparam_back = os.path.join(script_path_until_folder, 'data','gif','filterparam.gif')
    return filterparam_back

#DUDUL
def dudul_icon():
    script_path_until_folder = pathname()
    dudul_icon = os.path.join(script_path_until_folder, 'data', 'ico', 'dudul_icon.ico')
    return dudul_icon

def cdudul_back():
    script_path_until_folder = pathname()
    cdudul_back = os.path.join(script_path_until_folder, 'data', 'gif', 'cdudul_back.gif')
    return cdudul_back

def bdudul_back():
    script_path_until_folder = pathname()
    bdudul_back = os.path.join(script_path_until_folder, 'data', 'gif', 'bdudul_back.gif')
    return bdudul_back

#Type
def filterbytype_icon():
    script_path_until_folder = pathname()
    filterbytype_icon = os.path.join(script_path_until_folder, 'data','ico', 'selectbytype.ico')
    return filterbytype_icon

def cfilterbytype_back():
    script_path_until_folder = pathname()
    cfilterbytype_back = os.path.join(script_path_until_folder, 'data','gif', 'Filter.gif')
    return cfilterbytype_back

def bfilterbytype_back():
    script_path_until_folder = pathname()
    bfilterbytype_back = os.path.join(script_path_until_folder, 'data','gif', 'bFilter.gif')
    return bfilterbytype_back

#All elements in selected categories
def allelcat_icon():
    script_path_until_folder = pathname()
    allelcat_icon = os.path.join(script_path_until_folder, 'data','ico', 'All elements in selected categories.ico')
    return allelcat_icon

#All elements on selected levels
def level_icon():
    script_path_until_folder = pathname()
    level_icon = os.path.join(script_path_until_folder, 'data','ico', 'level_icon.ico')
    return level_icon

#Ownership of elements
def owned_icon():
    script_path_until_folder = pathname()
    owned_icon = os.path.join(script_path_until_folder, 'data','ico', 'owner_icon.ico')
    return owned_icon

#Unbound rooms
def unboundrooms_icon():
    script_path_until_folder = pathname()
    unboundrooms_icon = os.path.join(script_path_until_folder, 'data','ico', 'unboundrooms.ico')
    return unboundrooms_icon

#Mirrored doors
def unbounddoors_icon():
    script_path_until_folder = pathname()
    unbounddoors_icon = os.path.join(script_path_until_folder, 'data','ico', 'unbounddoors_icon.ico')
    return unbounddoors_icon

#Walk on Elements
def walkonelement_icon():
    script_path_until_folder = pathname()
    walkonelement_icon = os.path.join(script_path_until_folder, 'data','ico', 'walkonelements.ico')
    return walkonelement_icon

def cwalk_back():
    script_path_until_folder = pathname()
    cwalk_back = os.path.join(script_path_until_folder, 'data','gif', 'walkOnElements.gif')
    return cwalk_back

def bwalk_back():
    script_path_until_folder = pathname()
    bwalk_back = os.path.join(script_path_until_folder, 'data','gif', 'bwalk.png')
    return bwalk_back

#IDs from Excel
def excelid_back():
    script_path_until_folder = pathname()
    excelid_back = os.path.join(script_path_until_folder, 'data','gif', 'idselectlarg.png')
    return excelid_back

def excelid_icon():
    script_path_until_folder = pathname()
    excelid_icon = os.path.join(script_path_until_folder, 'data','ico', 'excel_icon.ico')
    return excelid_icon

def green_light():
    script_path_until_folder = pathname()
    green_light = os.path.join(script_path_until_folder, 'data','gif', 'ready.png')
    return green_light

def red_light():
    script_path_until_folder = pathname()
    red_light = os.path.join(script_path_until_folder, 'data','gif', 'not_ready.png')
    return red_light

#By ID (Reduce Selection)
def reduId_back():
    script_path_until_folder = pathname()
    reduId_bacK = os.path.join(script_path_until_folder, 'data','gif', 'id_manual.png')
    return reduId_bacK

def reduId_icon():
    script_path_until_folder = pathname()
    reduId_icon = os.path.join(script_path_until_folder, 'data','ico', 'id_manual.ico')
    return reduId_icon

#Bank
def bank():
    script_path_until_folder = pathname()
    bank = os.path.join(script_path_until_folder, 'data','bank')
    return bank

def cbank_back():
    script_path_until_folder = pathname()
    cbank_back = os.path.join(script_path_until_folder, 'data','gif','cbank.gif')
    return cbank_back

#Save
def save_icon():
    script_path_until_folder = pathname()
    save_icon = os.path.join(script_path_until_folder, 'data','ico','save_icon.ico')
    return save_icon

def save_back():
    script_path_until_folder = pathname()
    save_back = os.path.join(script_path_until_folder, 'data','gif','save_back.gif')
    return save_back

#Load
def loadselection_icon():
    script_path_until_folder = pathname()
    loadselection_icon = os.path.join(script_path_until_folder, 'data','ico','loadselection.ico')
    return loadselection_icon

#Import
def import_icon():
    script_path_until_folder = pathname()
    import_icon = os.path.join(script_path_until_folder, 'data','ico', 'import_icon.ico')
    return import_icon

def import_back():
    script_path_until_folder = pathname()
    import_back = os.path.join(script_path_until_folder, 'data','gif', 'import.png')
    return import_back

#Export
def export_icon():
    script_path_until_folder = pathname()
    export_icon = os.path.join(script_path_until_folder, 'data','ico','export_icon.ico')
    return export_icon

def cooexport_back():
    script_path_until_folder = pathname()
    cooexport_back = os.path.join(script_path_until_folder, 'data','gif','export2.gif')
    return cooexport_back

def borexport_back():
    script_path_until_folder = pathname()
    borexport_back = os.path.join(script_path_until_folder, 'data','gif','export.png')
    return borexport_back

def export_back():
    script_path_until_folder = pathname()
    export_back = os.path.join(script_path_until_folder, 'data','gif','export1.png')
    return export_back

#By ID (Deleters)
def delete_back():
    script_path_until_folder = pathname()
    delete_back = os.path.join(script_path_until_folder, 'data','gif', 'delete_back.gif')
    return delete_back

#By IDs from Excel (Deleters)
def delete_sym():
    script_path_until_folder = pathname()
    delete_sym = os.path.join(script_path_until_folder, 'data','sym', 'delete.png')
    return delete_sym

#All DirectShape elements (Deleters)
def directshapedelete_icon():
    script_path_until_folder = pathname()
    directshapedelete_icon = os.path.join(script_path_until_folder, 'data','ico', 'directshapedelete.ico')
    return directshapedelete_icon

#OST_Categories (Deleters)
def deleteostcategory_icon():
    script_path_until_folder = pathname()
    deleteostcategory_icon = os.path.join(script_path_until_folder, 'data','ico', 'deleteostcategory.ico')
    return deleteostcategory_icon

#Value of parameter for selected elements (Deleters)
def delparametervalueforselected_icon():
    script_path_until_folder = pathname()
    delparametervalueforselected_icon = os.path.join(script_path_until_folder, 'data','ico', 'delparametervalueforselected.ico')
    return delparametervalueforselected_icon

def del_pvalue_back():
    script_path_until_folder = pathname()
    del_pvalue_back = os.path.join(script_path_until_folder, 'data','gif', 'select_element.gif')
    return del_pvalue_back

def del_pvalue_icon():
    script_path_until_folder = pathname()
    del_pvalue_icon = os.path.join(script_path_until_folder, 'data','ico', 'select_element.ico')
    return del_pvalue_icon

#Desired character in  value of parameter for selected elements (Deleters)
def del_pval_character_icon():
    script_path_until_folder = pathname()
    del_pval_character_icon = os.path.join(script_path_until_folder, 'data','ico', 'delete_charcter.ico')
    return del_pval_character_icon


def del_pval_character_back():
    script_path_until_folder = pathname()
    del_pval_character_back = os.path.join(script_path_until_folder, 'data','gif', 'delete_charcter.png')
    return del_pval_character_back

#Delete parameter completely from model (Deleters)
def del_param_icon():
    script_path_until_folder = pathname()
    del_param_icon = os.path.join(script_path_until_folder, 'data','ico', 'delete_parameter_entierly.ico')
    return del_param_icon

def del_param_insert_icon():
    script_path_until_folder = pathname()
    del_param_insert_icon = os.path.join(script_path_until_folder, 'data','ico', 'insert_name.ico')
    return del_param_insert_icon

def del_param_insert_back():
    script_path_until_folder = pathname()
    del_param_insert_back = os.path.join(script_path_until_folder, 'data','gif', 'insert_name.png')
    return del_param_insert_back

def del_param_cat_back():
    script_path_until_folder = pathname()
    del_param_cat_back = os.path.join(script_path_until_folder, 'data','gif', 'category_op.png')
    return del_param_cat_back


def del_param_elem_back():
    script_path_until_folder = pathname()
    del_param_elem_back = os.path.join(script_path_until_folder, 'data','gif', 'element.png')
    return del_param_elem_back

#Check Parameter Against Category (Checkers)
def check_param_cat_icon():
    script_path_until_folder = pathname()
    check_param_cat_icon = os.path.join(script_path_until_folder, 'data','ico', 'check_param_cat_icon.ico')
    return check_param_cat_icon

def check_param_cat_back():
    script_path_until_folder = pathname()
    check_param_cat_back = os.path.join(script_path_until_folder, 'data','gif', 'check_param_cat_back.png')
    return check_param_cat_back

def check_param_cat_sym():
    script_path_until_folder = pathname()
    check_param_cat_sym = os.path.join(script_path_until_folder, 'data','sym', 'check_param_cat_sym.png')
    return check_param_cat_sym

#Script Executer
def dir_path():
    script_path_until_folder = pathname()
    dir_path = os.path.join(script_path_until_folder, 'data','set', 'dir.txt')
    return dir_path

def py_icon():
    script_path_until_folder = pathname()
    py_icon = os.path.join(script_path_until_folder, 'data','ico', 'pyexecuter.ico')
    return py_icon

def py_back():
    script_path_until_folder = pathname()
    py_back = os.path.join(script_path_until_folder, 'data','gif', 'py.gif')
    return py_back

def python_back():
    script_path_until_folder = pathname()
    python_back = os.path.join(script_path_until_folder, 'data','gif', 'Python.png')
    return python_back

def pylist_path():
    script_path_until_folder = pathname()
    pylist_path = os.path.join(script_path_until_folder, 'data', 'pylist')
    return pylist_path

def pydir_path():
    script_path_until_folder = pathname()
    pydir_path = os.path.join(script_path_until_folder, 'data', 'set')
    return pydir_path

#Extension settings
def icosetup():
    script_path_until_folder = pathname()
    icosetup = os.path.join(script_path_until_folder, 'data', 'ico', 'setup.ico')
    return icosetup

def backsetup():
    script_path_until_folder = pathname()
    backsetup = os.path.join(script_path_until_folder, 'data', 'gif', 'setup.gif')
    return backsetup

def setting_back():
    script_path_until_folder = pathname()
    setting_back = os.path.join(script_path_until_folder, 'data','gif', 'setting.gif')
    return setting_back

#User Manual
def usermanual_icon():
    script_path_until_folder = pathname()
    usermanual_icon = os.path.join(script_path_until_folder, 'data','ico', 'usermanual.ico')
    return usermanual_icon