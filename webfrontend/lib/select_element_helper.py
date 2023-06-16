class SelectElementHelper():
    """SelectElementHelper provides a helper method to simplify the generation of basic HTML elements """
    def __init__(self, labels:list, values:list, selected_value:None):
        
        self.values= [] if values is None else values
        #TODO check for type
        self.labels=[] if labels is None else labels
        if len(self.values) != len(self.labels):
            raise ValueError("The lables and values of the SELECT items should have the same length")
        pass
        self.selected_value = selected_value

    def select_element(self, class_name='', name='',id='',):
        html=''
        html+=f'<select class="{class_name}" name="{name}" id="{id}" >'
        for index in range(len(self.values)):
            option_value = self.values[index]
            option_label = self.labels[index]
            selected_attribute = '' if option_value != self.selected_value else 'selected'
            html+=f'<option value="{option_value}" {selected_attribute}>{option_label}</option>'
        html+='</select>'
        return html

