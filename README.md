Data Download
-------------

1. Please download and unzip: https://goo.gl/PXhGRK


PySpark Installation for Windows
--------------------------------
1. Download winutils from https://bit.ly/2NbXns4 - place it in C:/username/Downloads/hadoop/bin
2. Open Anaconda Propmt (Start Menu)
3. Create the folder C:\\tmp\\hive
3. Run the following steps:

```bash
> set HADOOP_HOME=C:\\username\\Downloads\\hadoop
> set PATH=%HADOOP_HOME%\\bin;%PATH%
> winutils.exe chmod -R 777 C:\\tmp\\hive
```

4. Locate the Spark folder (suppose it is C:\\username\\Downloads\\spark), and run:

```bash
> set SPARK_HOME=C:\\username\\Downloads\\spark
> set PATH=%SPARK_HOME%\\bin;%PATH%
> set PYSPARK_DRIVER_PYTHON=jupyter
> set PYSPARK_DRIVER_PYTHON_OPTS='notebooks'
```

Download and Install Tutorial Material
--------------------------------------

1. Download tutorial material from: https://bitbucket.org/jaidevd/ipec-fdp
2. Unzip downloaded folder to C:\\username\\Downloads\\ipec-fdp
3. Navigate to that folder from Anaconda prompt
4. Run `> conda install --file requirements.txt`
5. Run `> pyspark`
