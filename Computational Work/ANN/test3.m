arr_theta=0:1:180;
arr_phi=0:1:360;
phi=90;
arr_phi_reduced=80:1:100;
a=100e-9;
b=90e-9;
t=6e-9;
omega=(pi/4)*a*b*t;
Ndxx=0.8529;
Ndyy=0.0788;
Ndzz=0.0683;
Ms=8e5;
Hk=(Ndyy-Ndzz)*Ms;
Hd=(Ndxx-Ndyy)*Ms;
mu0=4*pi*1e-7;
q=1.602e-19;
%Hk=[0 0.2 0.2 0.7 1 1.4]
if true
        for Hz=[0 0.2 0.5 0.7 1 1.4]*Hk
            E=((0.5*mu0*Ms*Hk*omega*sind(arr_theta).^2)+(mu0*Ms*Hz*omega*cosd(arr_theta)))/q;
            plot(arr_theta,E,'LineWidth',2);
            xticks([0 45 90 135 180]);
            xlabel('\theta');
            ylabel('Energy (eV)');
            legend('Hz=0 Hk','Hz=0.2 Hk','Hz=0.5 Hk','Hz=0.7 Hk','Hz=1 Hk','Hz=1.4 Hk' );
            if Hz==0
                hold;
            end
        end  
end
