% import model

<!DOCTYPE html>
<html>

<body>

  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>
  
  <table>
   <tr>
    <td>

     <h2>{{igra.pravilni_del_gesla()}}</h2>
     Nepravilni ugibi: <b>{{igra.nepravilni_ugibi()}} </b>
    </td>

    <td> 
     <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje" />
    </td>
   </tr>
  </table>

  % if stanje == model.ZMAGA:

  <h1> ZMAGA! </h1>

  <form action= "/igra/" method ="post">
   <button type="submit">Nova igra</button>
  </form>

  % elif stanje == model.PORAZ: 
   <h1> IZGUBILI STE! </h1>
   Pravilno geslo: <h4> {{igra.geslo}} </h4>

 <form action= "/igra/" method ="post">
   <button type="submit">Nova igra</button>
  </form>
  
  % else:
   

  

  <form action="/igra/{{id_igre}}/" method="POST">
  Črka: <input type= "text" name="crka">
    <button type="submit">Pošlji ugib</button>
  </form>

  %end

</body>

</html>