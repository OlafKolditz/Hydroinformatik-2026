#include <vector>
//#include <cmath>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
  //1-Definitionen
  //1.1 Diskretisierung
  double dt,dx;
  int nj = 101;
  int nt = 1000;
  vector<double> u_new, u_old;
  u_new.resize(nj);
  u_old.resize(nj);  
  double Ne;
  double x,y,alpha=1.,t=1;
  std::ofstream out_file;
  out_file.open("out.csv");
  //2-Anfangsbedingungen
  for(int ix=0;ix<nj;ix++)
  {
    u_old[ix] = 0.;
  }
  //3-Randbedingungen
  double u_bc_l = 3.;
  double u_bc_r = -3.;
  u_new[0] = u_old[0] = u_bc_l;
  u_new[nj-1] = u_old[nj-1] = u_bc_r;
  //4-Diskretisierung
  //dt = 1.;
  dx = 1./(nj-1);
  // 4 Formel
  dt = 0.5 * dx*dx / alpha * 1.; // Zeitschrittsteuerung
  Ne = alpha * dt / (dx*dx);  
  //------------------------------------------------------
  //2-Berechnung
  for(int t=0;t<nt;t++)
  {
    for(int ix=1;ix<nj-1;ix++)
    {
      u_new[ix] = u_old[ix] + Ne * (u_old[ix-1] - 2*u_old[ix] + u_old[ix+1]);
    }  
    // Daten speichern
    for(int i=1;i<nj-1;i++)
    {
      u_old[i] = u_new[i];
    }	
	if(t%100==0)
	{
    for(int ix=0;ix<nj;ix++)
    {
	  {
        x = dx*ix;
        out_file << x << "," << u_new[ix] << endl;
	  }
    }  
	}
  }  
}
//HW1 Lösung: y=sin(sqrt(pi*alpha)*x) * exp(-pi*t) plotten
//HW2 Lösung: y=sin(pi/sqrt(alpha)*x) * exp(-pi*pi*t) plotten
//HW3 Lösung: y=sin(pi*x) * exp(-alpha*pi*pi*t) plotten
//HW4 Lösungen vergleichen
//HW5 Verschiedene Zeiten (aus Eingabedatei) lesen und rechnen
