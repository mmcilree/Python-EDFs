group_tables = [ [ [ [ 1, 2, 3 ], [ 2, 3, 1 ], [ 3, 1, 2 ] ] ], 
  [ [ [ 1, 2, 3, 4 ], [ 2, 3, 4, 1 ], [ 3, 4, 1, 2 ], [ 4, 1, 2, 3 ] ], 
      [ [ 1, 2, 3, 4 ], [ 2, 1, 4, 3 ], [ 3, 4, 1, 2 ], [ 4, 3, 2, 1 ] ] ], 
  [ [ [ 1, 2, 3, 4, 5 ], [ 2, 3, 4, 5, 1 ], [ 3, 4, 5, 1, 2 ], [ 4, 5, 1, 2, 3 ], [ 5, 1, 2, 3, 4 ] ] ],
  [ [ [ 1, 2, 3, 4, 5, 6 ], [ 2, 3, 1, 6, 4, 5 ], [ 3, 1, 2, 5, 6, 4 ], [ 4, 5, 6, 1, 2, 3 ], 
          [ 5, 6, 4, 3, 1, 2 ], [ 6, 4, 5, 2, 3, 1 ] ], 
      [ [ 1, 2, 3, 4, 5, 6 ], [ 2, 3, 4, 5, 6, 1 ], [ 3, 4, 5, 6, 1, 2 ], [ 4, 5, 6, 1, 2, 3 ], 
          [ 5, 6, 1, 2, 3, 4 ], [ 6, 1, 2, 3, 4, 5 ] ] ], 
  [ [ [ 1, 2, 3, 4, 5, 6, 7 ], [ 2, 3, 4, 5, 6, 7, 1 ], [ 3, 4, 5, 6, 7, 1, 2 ], 
          [ 4, 5, 6, 7, 1, 2, 3 ], [ 5, 6, 7, 1, 2, 3, 4 ], [ 6, 7, 1, 2, 3, 4, 5 ], 
          [ 7, 1, 2, 3, 4, 5, 6 ] ] ], 
  [ [ [ 1, 2, 3, 4, 5, 6, 7, 8 ], [ 2, 3, 4, 5, 6, 7, 8, 1 ], [ 3, 4, 5, 6, 7, 8, 1, 2 ], 
          [ 4, 5, 6, 7, 8, 1, 2, 3 ], [ 5, 6, 7, 8, 1, 2, 3, 4 ], [ 6, 7, 8, 1, 2, 3, 4, 5 ], 
          [ 7, 8, 1, 2, 3, 4, 5, 6 ], [ 8, 1, 2, 3, 4, 5, 6, 7 ] ], 
      [ [ 1, 2, 3, 4, 5, 6, 7, 8 ], [ 2, 3, 4, 1, 8, 7, 5, 6 ], [ 3, 4, 1, 2, 6, 5, 8, 7 ], 
          [ 4, 1, 2, 3, 7, 8, 6, 5 ], [ 5, 8, 6, 7, 3, 1, 2, 4 ], [ 6, 7, 5, 8, 1, 3, 4, 2 ], 
          [ 7, 5, 8, 6, 2, 4, 1, 3 ], [ 8, 6, 7, 5, 4, 2, 3, 1 ] ], 
      [ [ 1, 2, 3, 4, 5, 6, 7, 8 ], [ 2, 3, 4, 1, 8, 5, 6, 7 ], [ 3, 4, 1, 2, 7, 8, 5, 6 ], 
          [ 4, 1, 2, 3, 6, 7, 8, 5 ], [ 5, 6, 7, 8, 1, 2, 3, 4 ], [ 6, 7, 8, 5, 4, 1, 2, 3 ], 
          [ 7, 8, 5, 6, 3, 4, 1, 2 ], [ 8, 5, 6, 7, 2, 3, 4, 1 ] ], 
      [ [ 1, 2, 3, 4, 5, 6, 7, 8 ], [ 2, 3, 4, 1, 7, 8, 6, 5 ], [ 3, 4, 1, 2, 6, 5, 8, 7 ], 
          [ 4, 1, 2, 3, 8, 7, 5, 6 ], [ 5, 8, 6, 7, 3, 1, 2, 4 ], [ 6, 7, 5, 8, 1, 3, 4, 2 ], 
          [ 7, 5, 8, 6, 4, 2, 3, 1 ], [ 8, 6, 7, 5, 2, 4, 1, 3 ] ], 
      [ [ 1, 2, 3, 4, 5, 6, 7, 8 ], [ 2, 1, 5, 6, 3, 4, 8, 7 ], [ 3, 5, 1, 7, 2, 8, 4, 6 ], 
          [ 4, 6, 7, 1, 8, 2, 3, 5 ], [ 5, 3, 2, 8, 1, 7, 6, 4 ], [ 6, 4, 8, 2, 7, 1, 5, 3 ], 
          [ 7, 8, 4, 3, 6, 5, 1, 2 ], [ 8, 7, 6, 5, 4, 3, 2, 1 ] ] ], 
  [ [ [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ], [ 2, 3, 4, 5, 6, 7, 8, 9, 1 ], [ 3, 4, 5, 6, 7, 8, 9, 1, 2 ], 
          [ 4, 5, 6, 7, 8, 9, 1, 2, 3 ], [ 5, 6, 7, 8, 9, 1, 2, 3, 4 ], [ 6, 7, 8, 9, 1, 2, 3, 4, 5 ], 
          [ 7, 8, 9, 1, 2, 3, 4, 5, 6 ], [ 8, 9, 1, 2, 3, 4, 5, 6, 7 ], [ 9, 1, 2, 3, 4, 5, 6, 7, 8 ] ],
      [ [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ], [ 2, 3, 1, 6, 9, 8, 5, 4, 7 ], [ 3, 1, 2, 8, 7, 4, 9, 6, 5 ], 
          [ 4, 6, 8, 5, 1, 9, 3, 7, 2 ], [ 5, 9, 7, 1, 4, 2, 8, 3, 6 ], [ 6, 8, 4, 9, 2, 7, 1, 5, 3 ], 
          [ 7, 5, 9, 3, 8, 1, 6, 2, 4 ], [ 8, 4, 6, 7, 3, 5, 2, 9, 1 ], [ 9, 7, 5, 2, 6, 3, 4, 1, 8 ] ] 
     ], 
  [ [ [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], [ 2, 3, 4, 5, 1, 10, 6, 7, 8, 9 ], 
          [ 3, 4, 5, 1, 2, 9, 10, 6, 7, 8 ], [ 4, 5, 1, 2, 3, 8, 9, 10, 6, 7 ], 
          [ 5, 1, 2, 3, 4, 7, 8, 9, 10, 6 ], [ 6, 7, 8, 9, 10, 1, 2, 3, 4, 5 ], 
          [ 7, 8, 9, 10, 6, 5, 1, 2, 3, 4 ], [ 8, 9, 10, 6, 7, 4, 5, 1, 2, 3 ], 
          [ 9, 10, 6, 7, 8, 3, 4, 5, 1, 2 ], [ 10, 6, 7, 8, 9, 2, 3, 4, 5, 1 ] ], 
      [ [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 1 ], 
          [ 3, 4, 5, 6, 7, 8, 9, 10, 1, 2 ], [ 4, 5, 6, 7, 8, 9, 10, 1, 2, 3 ], 
          [ 5, 6, 7, 8, 9, 10, 1, 2, 3, 4 ], [ 6, 7, 8, 9, 10, 1, 2, 3, 4, 5 ], 
          [ 7, 8, 9, 10, 1, 2, 3, 4, 5, 6 ], [ 8, 9, 10, 1, 2, 3, 4, 5, 6, 7 ], 
          [ 9, 10, 1, 2, 3, 4, 5, 6, 7, 8 ], [ 10, 1, 2, 3, 4, 5, 6, 7, 8, 9 ] ] ] ]