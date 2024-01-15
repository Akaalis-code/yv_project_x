# Algorithm and Flowcharts
![overview of project](https://raw.githubusercontent.com/Akaalis-code/yv_project_x/55499c169778ab91e33fc2080ca609921f5ad8af/yv_backend/yv_storage_area/overview_in_svg.svg)



## Steps that are being implemented from backend
- Terminology : 
    - Smallest possible action that a body can take is called "GENE"  
    - Series of genes that an object needs to take is collectively called as "DNA"  
    - Each Gene has one of five possible actions (STOP-0 , RIGHT-1 , LEFT-2 , UP-3 , DOWN-4)  
  
  
1. Have Initial population of "x" where each DNA contains "n" genes
2. Let them perfom according to their DNA
3. Based on their acheiments (final distance from the destination point) all "x" population will be sorted 
4. Top "y" number of performers ( where "y"<"x" ) will be selected and least "x-y" performers DNA will be deleted
5. Now the "y" performers will be randomly paired in 2 to mingle their GENES to create child DNA of population "x" 
6. Once Child DNA is ready we will give each GENE of every DNA some chance to mutate into one of the allowed GENE
7. After mutation , the Child DNA s are allowed to perform and fed through step 1 
8. We will set a limit on for how many generations this (1 -> 7 -> 1) loop should go on 



## Initial thought process for establishing communication between front and backend 

1. Initial data structure will be like this as a ROW

| Unique_id     | Generation_id | DNA            |dist_body_dest   |communication_direction|
|:-------------:|:-------------:|:--------------:|:---------------:|:---------------------:|
| g11           | g1            | 1232140....430 | 10              | 0                     |
| g12           | g1            | 1232140....430 | 100             | 0                     |
| g21           | g2            | 1232140....430 | 5               | 1                     |


- Terminology for above data :  
    - Unique_id = str(Generation_id)+str(value between 1 to X)  {info generated at back end}
    - Generation_id = 'g' followed by a number (1 to maximum generations you want to run) {info generated at backend}
    - DNA = sequence of genes with a length of whatever we decided {info generated at back end}
    - dist_body_dest = after allowing to perform and at the very end what is the final distance between body and destination {info generated at frontend }  
    - communication_direction = 0 (if rows are being created by front end ) 1 (if reverse) {info generated at both backend}