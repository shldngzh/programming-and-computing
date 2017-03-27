### hash merge

```sas
data output.result;
    length var1 var2 8.;
    call missing(var1, var2);
    
    decalre hash finder(dataset:"input.hash_table");
    finder.defineKey("var1");
    finder.defineData("var2");
    finder.defineDone();
    
    set input.ds;
    
    if finder.find()=0 then do;
        tag = 1;
    end;
    
run;

```
