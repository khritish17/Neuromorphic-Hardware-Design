load("mnist.mat");

y = zeros(50000,10);

for i = 1:60000
    g = trainY(1,i);
    y(i,g+1)=1;
end



n_hidden_neurons = 50;
Eta = 0.01;
 w1 = randn(784,n_hidden_neurons) ;
w2 = randn(n_hidden_neurons,10) ;
b1 = randn(1,n_hidden_neurons);
b2 = randn(1,10) ;
delta1 = zeros(784,n_hidden_neurons);
delta2 = zeros(n_hidden_neurons,10);
del1 = zeros(n_hidden_neurons,1);
del2 = zeros(10,1);

for i = 1:60000
    a1 = trainX(i,:)';
    a4 = double(a1);
    a2 = sigmoid(a4'*w1 + b1);
    a3 = sigmoid(a2*w2 + b2);
    del2 = a3 - y(i,:);
   err(1,i) = sum((a3-y(i,:)).^2);
    del1 = w2*del2';
    delta1 = delta1 + a4*(del1');
    delta2 = delta2 + a2'*del2;
    

    w1 = w1 - (Eta/60000)*delta1;    
    w2 = w2 - (Eta/60000)*delta2;

    b1 = b1 - Eta*del1';

    b2 = b2 - Eta*del2;
    i/600
    
end






    
    
    
    
    
    
    
    
    
 
