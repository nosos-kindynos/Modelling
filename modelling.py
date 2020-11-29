# import data from csv file with {person:[(contact,risk), ....]},...}



from functions import *

def model_data_to_weighted_dyadic_relationships(vertices,data):

    def convert_data_to_risk_mapping(data):
        average_deviation_of_vertex={}
        for person in data:
            total_deviation=[]
            for contact in data.get(person):
                found=False
                for i in data.get(contact[0]):
                    if i[0]==person:
                        found=True
                        deviation=(abs((contact[1]-i[1])))/1.66
                        break
                if found==False:
                    deviation=(abs((contact[1])))/1.66

                total_deviation.append(deviation)
            avg_deviation=average(total_deviation)
            average_deviation_of_vertex.update({person: avg_deviation})

        print(average_deviation_of_vertex)

        risk_mapping={}
        for person in data:
            for contact in data.get(person):
                if get_risk((person,contact[0]),risk_mapping)==None:
                    for i in data.get(contact[0]):
                        if i[0]==person:
                            b = [average_deviation_of_vertex.get(
                                i[0]), average_deviation_of_vertexs.get(contact[0])]
                            risk=weighted_average(i[1],contact[1],b)
                            break
                    

                    risk_mapping.update({(person,contact[0]):risk})

        return(risk_mapping)


    def convert_risk_mapping_to_mapping(vertices,risk_mapping):
        mapping={}
        for vertex in vertices:
            first_degree_connections=[]
            for edge in risk_mapping:
                if vertex in edge:
                    first_degree_connections.append(other_vertex(vertex,edge))
            mapping.update({vertex:first_degree_connections})
        return([mapping,risk_mapping])

    return(convert_risk_mapping_to_mapping(vertices,convert_data_to_risk_mapping(data)))



a = 0.9
k = {1: [(2, a), (3, a), (5, a), (6, a), (7, a)], 2: [(1, 0.3), (5, 0.2), (6, 0.1), (7, 0.4)], 3: [(1, a), (2, a), (4, a), (5, a), (6, a), (7, a)], 4: [
    (5, a)], 5: [(2, a), (3, a), (7, a)], 6: [(1, a), (2, a), (5, a), (7, a)], 7: [(1, a), (2, a), (3, a), (4, a), (5, a), (6, a)]}

m=model_data_to_weighted_dyadic_relationships([1,2,3,4,5,6,7],k)
print(m)



            
