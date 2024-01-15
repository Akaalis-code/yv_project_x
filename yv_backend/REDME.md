# Algorithm and Flowcharts
![overview of project](https://github.com/Akaalis-code/yv_project_x/blob/yv_dev_branch/yv_backend/yv_storage_area/overview.jpg)



## Steps that are being implemented from backend
Terminology : Smallest possible action that a body can take is called "GENE"  
              Series of genes that an object needs to take is collectively called as "DNA"  
              Each Gene has one of five possible actions (STOP-0 , RIGHT-1 , LEFT-2 , UP-3 , DOWN-4)  
  
  
1. Have Initial population of "x" where each DNA contains "n"" genes
2. Let them perfom according to their DNA
3. Based on their acheiments (final distance from the destination point) all "x" population will be sorted 
4. Top "y" number of performers ( where "y"<"x" ) will be selected and least "x-y" performers DNA will be deleted
5. Now the "y" performers will be randomly paired in 2 to mingle their GENES to create child DNA of population "x" 
6. Once Child DNA is ready we will give each GENE of every DNA some chance to mutate into one of the allowed GENE
7. After mutation , the Child DNA s are allowed to perform and fed through step 1 
8. We will set a limit on for how many generations this (1 -> 7 -> 1) loop should go on 