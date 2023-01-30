% Import the data
train_data=readmatrix('train.csv');
IP_trn=train_data(:,1:35);
OP_trn=train_data(:,36:61);

% Set the neural architecture
IP_dim=size(IP_trn, 2);     % Number of input nodes
OP_dim=size(OP_trn, 2);     % Number of output nodes
%OP_dim=2;
hidden_dim=[2, 2];          % Number of hidden layer and hidden neurons
epoch=1000;

% Transpose the IP and OP matrix
IP_trn=IP_trn';
OP_trn=OP_trn';

% Initializing weights
weight_matrix_count=length(hidden_dim)+1;
for i=1:weight_matrix_count
    if i==1
        weight=rand(IP_dim, hidden_dim(i))
    elseif i==weight_matrix_count
        weight=rand(hidden_dim(i-1), OP_dim)
    else
        weight=rand(hidden_dim(i-1),hidden_dim(i))
    end
    filename=['wt',sprintf('%d',i),'.mat'];
    save(filename,'weight');
end

% Initializing bias
bias_count=sum(hidden_dim) + OP_dim;
bias_dim=rand(1,bias_count)

% Forward propagation


% Backpropagation