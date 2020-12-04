from functions import *


def model_data_to_weighted_dyadic_relationships(average_transfer_chance, data):

    def convert_data_to_risk_mapping(data):
        average_deviation_of_vertex = {}
        for person in data:
            total_deviation = []
            for contact in data.get(person):
                found = False
                contact_data = data.get(contact[0])
                if contact_data!=None:
                    for i in contact_data:
                        if i[0] == person:
                            found = True
                            deviation = (abs((contact[1]-i[1])))/1.66
                            break
                if found == False: 
                    deviation=(abs((contact[1])))/1.66

                total_deviation.append(deviation)


            avg_deviation = average(total_deviation)
            average_deviation_of_vertex.update({person: avg_deviation})

        risk_mapping = {}
        for person in data:
            for contact in data.get(person):
                if get_risk((person, contact[0]), risk_mapping) == None:
                    found=False
                    contact_data = data.get(contact[0])
                    if contact_data != None:
                        for i in contact_data:
                            if i[0] == person:
                                b = [average_deviation_of_vertex.get(person), average_deviation_of_vertex.get(contact[0])]
                                risk = weighted_average(contact[1], i[1], b)
                                found=True
                                break
                    if found==False:
                        if average_deviation_of_vertex.get(contact[0])!=None:
                            b = [average_deviation_of_vertex.get(person), average_deviation_of_vertex.get(contact[0])]
                            risk = weighted_average(0, contact[1], b)
                        else:
                            risk=contact[1]

                    risk_mapping.update({(person, contact[0]): risk*average_transfer_chance})

        return(risk_mapping)

    def convert_risk_mapping_to_mapping(risk_mapping):
        vertices=[]
        for edge in risk_mapping:
            for i in edge:
                if i not in vertices:
                    vertices.append(i)
        
        mapping = {}
        for vertex in vertices:
            first_degree_connections = []
            for edge in risk_mapping:
                if vertex in edge:
                    first_degree_connections.append(other_vertex(vertex, edge))
            mapping.update({vertex: first_degree_connections})
        return([mapping, risk_mapping,vertices])

    return(convert_risk_mapping_to_mapping(convert_data_to_risk_mapping(data)))

