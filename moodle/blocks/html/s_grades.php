<?php
$con=mysqli_connect("");
$sql="select s_name from student";
$result=mysqli_query($con,$sql);
$row=mysqli_fetch_array($result);

$s_name=$row["s_name"];
echo $s_name;

mysqli_close(conn);

?>
<div>
<?=$s_name?>
</div>
</body>
</html>
