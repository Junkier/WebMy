INSERT INTO "Emp" VALUES ("7369","Smith","Clerk","7902","1980-12-17","800",null,"20");
INSERT INTO "Emp" VALUES ("7499","Allen","Salesman","7698","1981-02-20","1600",null,"20");
INSERT INTO "Emp" VALUES ("7521","Ward","Salesman","7698","1981-02-22","1250","500","30");
INSERT INTO "Emp" VALUES ("7566","Jones","Manager","7839","1981-04-02","2975",null,"20");
INSERT INTO "Emp" VALUES ("7654","Martin","Salesman","7698","1981-09-28","2850",null,"30");
INSERT INTO "Emp" VALUES ("7782","Clark","Manager","7839","1981-06-09","2450",null,"10");
INSERT INTO "Emp" VALUES ("7788","Scott","Analyst","7566","1982-12-09","3000",null,"20");
INSERT INTO "Emp" VALUES ("7839","King","president","7698","1981-11-17","5000",null,"10");

Emp.objects.create(Empno='7839',Ename='King',Job='president',Mgr='7698',HireDate='1981-11-17',Sal='5000',Deptno='10')
Empno
Ename
Job
Mgr
HireDate
Sal
Deptno