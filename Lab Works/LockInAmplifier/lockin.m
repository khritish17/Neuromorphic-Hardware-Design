Wsig=12;
theta_sig=45;
vsig=2;
t=-5:0.1:5;
Vsig=vsig.*sin(Wsig.*t + theta_sig);
plot(Vsig,t);