% This matlab code is a support to the character_recog.mlx
% Here we wish to find the optimal neuron size in the hidden layer

% -------- Importing the training data --------
train_data=readmatrix('train.csv');
x_train=train_data(:,1:35); % I/P for trainging 
t_train=train_data(:,36:61); % target for training 

% -------- Importing the testing data --------
test_data=readmatrix('test.csv');
x_test=test_data(:,1:35);   % I/P for testing
t_test=test_data(:,36:61);  % target for testing

% -------- Data Pre-processing --------
x_trainT=x_train';
t_trainT=t_train';

x_testT=x_test';
t_testT=t_test';

% We will define the Neural architecture, but instead of hard coding 
% we will iterate from hidden size of hidden layer from 20 to 200
% And will choose that neuron size for which both training and validation
% error are equal

%!!!!!!!!!!!!!!!!!!!!!
run=30
final_test_data=zeros(1,run);
for i=1:run
    display(i)
    min_neuron=1;
    max_neuron=200;
    test_error=zeros(1,max_neuron-min_neuron);
    for hidden_neuron=min_neuron:max_neuron
        %------- The Neural Architecture-------
        hiddenLayer=[hidden_neuron];
        net=patternnet(hiddenLayer);
        net.divideParam.trainRatio=100/100;
        net.divideParam.testRatio=0;
        net.divideParam.valRatio=0;
        % ---- Training the Neural Network -------
        net=train(net, x_trainT, t_trainT);
    
        %-------- Saving the error--------------
        test_output=net(x_testT);
        test_error(hidden_neuron)=perform(net, t_testT, test_output);
        %test_error(hidden_neuron)=mean(sqrt(mean( (t_testT-test_output).^2 )));
    end
    [mtest,itest]=min(test_error);
    final_test_data(i)=itest;
    
end
histogram(final_test_data)



