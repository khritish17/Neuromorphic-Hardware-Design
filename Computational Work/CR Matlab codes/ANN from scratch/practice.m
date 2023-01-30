

for i =1:3
    weight=zeros(2,2)
    filename=['wt',sprintf('%d',i),'.mat'];
    save(filename,'weight');
end

a=rand(3,3)