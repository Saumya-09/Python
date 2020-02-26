# MongoDB

MongoDB is an open source database management system (DBMS) that uses a document-oriented database model which supports various forms of data.
A record in MongoDB is a document, which is a data structure composed of field and value pairs. MongoDB documents are similar to JavaScript Object Notation objects but use a variant called Binary JSON (BSON) that accommodates more data types. The fields in documents are akin to the columns in a relational database, and the values they contain can be a variety of data types, including other documents, arrays and arrays of documents, according to the MongoDB user manual.

Documents, which also must incorporate a primary key as a unique identifier, are the basic unit of data in MongoDB. Collections contain sets of documents and function as the equivalent of relational database tables. Collections can contain any type of data, but the restriction is the data in a collection cannot be spread across different databases.

## Key Components of MongoDB Architecture

-  _id – This is a field required in every MongoDB document. The _id field represents a unique value in the MongoDB document. The _id field is like the document's primary key. If you create a new document without an _id field, MongoDB will automatically create the field. So for example, if we see the example of the above customer table, Mongo DB will add a 24 digit unique identifier to each document in the collection.

- Collection – This is a grouping of MongoDB documents. A collection is the equivalent of a table which is created in any other RDMS such as Oracle or MS SQL. A collection exists within a single database. As seen from the introduction collections don't enforce any sort of structure.
- Cursor – This is a pointer to the result set of a query. Clients can iterate through a cursor to retrieve results.
- Database – This is a container for collections like in RDMS wherein it is a container for tables. Each database gets its own set of files on the file system. A MongoDB server can store multiple databases.
- Document - A record in a MongoDB collection is basically called a document. The document, in turn, will consist of field name and values.
- Field - A name-value pair in a document. A document has zero or more fields. Fields are analogous to columns in relational databases.

### Difference between MongoDB & RDBMS

Difference

- Table	Collection	In RDBMS, the table contains the columns and rows which are used to store the data whereas, in MongoDB, this same structure is known as a collection. The collection contains documents which in turn contains Fields, which in turn are key-value pairs.
- Row	Document	In RDBMS, the row represents a single, implicitly structured data item in a table. In MongoDB, the data is stored in documents.
- Column	Field	In RDBMS, the column denotes a set of data values. These in MongoDB are known as Fields.
- Joins	Embedded documents	In RDBMS, data is sometimes spread across various tables and in order to show a complete view of all data, a join is sometimes formed across tables to get the data. In MongoDB, the data is normally stored in a single collection, but separated by using Embedded documents. So there is no concept of joins in MongoDB.


### Advantages of MongoDB over RDBMS
- Schema less − MongoDB is a document database in which one collection holds different documents. Number of fields, content and size of the document can differ from one document to another.

- Structure of a single object is clear.

- No complex joins.

- Deep query-ability. MongoDB supports dynamic queries on documents using a document-based query language that's nearly as powerful as SQL.

- Tuning.

- Ease of scale-out − MongoDB is easy to scale.

- Conversion/mapping of application objects to database objects not needed.

- Uses internal memory for storing the (windowed) working set, enabling faster access of data.

### Why Use MongoDB?
- Document Oriented Storage − Data is stored in the form of JSON style documents.

- Index on any attribute

- Replication and high availability

- Auto-sharding

- Rich queries

- Fast in-place updates

- Professional support by MongoDB

### Where to Use MongoDB?
- Big Data
- Content Management and Delivery
- Mobile and Social Infrastructure
- User Data Management
- Data Hub

To show all database
>>> show dbs

to create database
>>> use (database_name)

To create user
>>>db.createUser({
	user:"rachit",
	pwd:"yagnik",
	roles:["readWrite","dbAdmin"]
});

To insert data
>>>{
	first_name:"Mangy",
	last_name:"Carl",
	contacts:[123456,567890],
	address:{
	house:"221B",
	street:"Baker Street",
	city:"London"sni
	}
}

To insert multiple values
>>>[{
	first_name:"Ken",
	last_name:"Adams",
	contacts:[123,590],
	address:{
	house:"4B",
	street:"Caltech Street",
	city:"Los Angeles"
	}
},{
	first_name:"Doug",
	last_name:"Judy",
	contacts:[1236,890],
	address:{
	house:"99",
	street:"One Police Plaza",
	city:"Brroklyn"
	},
	gender:"Male"
}]

To update an entry

>>> db.customer.update({first_name:"Mangy"},{$set:{gender:"Female"}});


To add a field
>>> db.customer.update({},{$set:{age:18}},false,true);

To increment a particular value

>>> db.customer.update({first_name:"Doug"},{$inc:{age:5}});


To remove a field
>>> db.customer.update({first_name:"Mangy"},{$unset:{gender:1}});

To upsert a value
>>> db.customer.update({first_name:"Mary"},{first_name:"Mary",last_name:"Jane"},{upsert: true});


To Rename a Column

>>> db.customer.update({},{$rename:{"gender":"sex"}},false,true);


To remove an entry

>>> db.customer.remove({first_name:"Mary"});


To remove only one particular entry

>>> db.customer.remove({first_name:"Mary"},{justOne:true});
