% This matlab code is a support to the character_recog.mlx
% Here we wish to find the optimal neuron size in the hidden layer

% -------- Importing the training data --------
train_data=readmatrix('train.csv');
x_train=train_data(:,1:35); % I/P for trainging 
t_train=train_data(:,36:61); % target for training 

% -------- Importing the testing data --------
test_data=readmatrix('noisy_test.csv');
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


min_neuron=1;
max_neuron=200;
train_error=zeros(1,max_neuron-min_neuron);
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
    train_output=net(x_trainT);
    train_error(hidden_neuron)=mse(net, t_trainT, train_output);
    %train_error(hidden_neuron)=mean(sqrt(mean( (t_trainT-train_output).^2 )));
    test_output=net(x_testT);
    test_error(hidden_neuron)=mse(net, t_testT, test_output);
    %test_error(hidden_neuron)=mean(sqrt(mean( (t_testT-test_output).^2 )));
end

plot(min_neuron:max_neuron, train_error,'r'); hold on;
plot(min_neuron:max_neuron, test_error,'b'); hold off;

[mtest,itest]=min(test_error);
disp(['The Min. value for test error is ' num2str(mtest) ' at neuron count ' num2str(itest)]  );
[mtrain,itrain]=min(train_error);
disp(['The Min. value for train error is ' num2str(mtrain) ' at neuron count ' num2str(itrain)]  );
