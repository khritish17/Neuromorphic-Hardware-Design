load("mnist.mat");
ct = 0 ;
%SET RANDOMDIG TO THE ANY NUMBER BETWEEN 1 and 10000
%This is the test images for testing the neural network which has 10000
%digits


randomdig=120;
for i = randomdig
    a4 = testX(i,:);
    img = reshape(a4, 28, 28)';
    image(img);
    hold on;
    a5 = double(a4);
    
    a6 = sigmoid(a5*w1 + b1);
    a7 = sigmoid(a6*w2 + b2);
    
    [z,ind]=max(a7);
    
   if (ind-1) == double(testY(1,i))
        ct = ct + 1 ;
   end
    %i/100;
    disp('Prediction By NeuralNetwork Below')
    ind-1
    disp('Actual DIGIT in Image')
   %double(testY(1,i))
end
ct/100;

    

