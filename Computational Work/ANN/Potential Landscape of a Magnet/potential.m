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
if true
        [theta,phi]=meshgrid(arr_theta,arr_phi);
        E_shape=0.5*mu0*Ms*(Hk+Hd.*cosd(phi).^2)*omega.*sind(theta).^2/q;  
        mesh(arr_theta,arr_phi,E_shape);
        xticks([0 30 60 90 120 150 180]);
         %xlabel('\theta');
        yticks([0 90 180 270 360]);
         %ylabel('\phi');
       
    end