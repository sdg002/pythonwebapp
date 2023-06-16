class SelectElementHelper():
    """docstring for SelectElementHelper provides a helper method to simplify the generation of basic HTML elements """
    def __init__(self, labels:list, values:list):
        self.values= [] if values is None else values
        #TODO check for type
        self.labels=[] if labels is None else labels
        if len(self.values) != len(self.labels):
            raise ValueError("The lables and values of the SELECT items should have the same length")
        pass

    def select_element(self, class_name='', name='',id='',):
        html=''
        html+=f'<select class="{class_name}" name="{name}" id="{id}" >'
        for index in range(len(self.values)):            
            html+=f'<option value="{self.values[index]}">{self.labels[index]}</option>'
        html+='</select>'
        return html

