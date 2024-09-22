def crab_left_right_from_unmarked_polygon(folded_train, list_of_all_the_vertices_in_marked_polygon_folded, just_the_marked_polygons_folded, list_of_all_the_vertices_in_unmarked_polygon_folded, just_the_unmarked_polygons_folded,other_polygon,other_vertex, vertices_of_polygons_to_the_right, vertices_of_polygons_to_the_left):
    crab_left = False
    crab_right = False
    other_polygon_except_other_vertex = other_polygon.copy()
    other_polygon_except_other_vertex.remove(other_vertex)
    for v in other_polygon_except_other_vertex: #go through all the vertices of other_polygon, which is an unmarked polygon
        neighbors = folded_train.graph.neighbors(v) #for each vertex of other_polygon, look at its neighbors
        for n in neighbors:
            if n in list_of_all_the_vertices_in_marked_polygon_folded:
                if n in vertices_of_polygons_to_the_right:
                    crab_right = True
                if n in vertices_of_polygons_to_the_left:
                    crab_left = True
                if crab_left == True and crab_right == True:
                    return [True,True]
            else: #neighbor of v is at an unmarked polygon
                list_of_unmarked_polyogns_to_check = []
                for p in just_the_unmarked_polygons_folded:
                    if n in p:
                        p_copy = p.copy()
                        p_copy.remove(n)
                        list_of_unmarked_polyogns_to_check.append(p_copy) #technically not polygons b.c. we remove n
                        break
                we_need_to_check_more = True
                check_counter = 0
                while we_need_to_check_more == True:
                    we_need_to_check_more = False
                    for p in list_of_unmarked_polyogns_to_check[check_counter:]:
                        for ver in p:
                            ne = folded_train.graph.neighbors(ver)
                            for nee in ne:
                                if nee in list_of_all_the_vertices_in_marked_polygon_folded:
                                    if n in vertices_of_polygons_to_the_right:
                                        crab_right = True
                                    if n in vertices_of_polygons_to_the_left:
                                        crab_left = True
                                    if crab_left == True and crab_right == True:
                                        return [True,True]
                                else:
                                    we_need_to_check_more = True
                                    for pee in just_the_unmarked_polygons_folded:
                                        if nee in pee:
                                            pee_copy = pee.copy()
                                            pee_copy.remove(nee)                                 
                                            list_of_unmarked_polyogns_to_check.append(pee_copy)
                                            break
            if crab_left == True and crab_right == True:
                return [True,True]
    
        if crab_left == True and crab_right == True:
            return [True,True]
            
    return [crab_left,crab_right]