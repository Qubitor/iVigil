import MySQLdb
con=MySQLdb.connect("localhost","root","test","face_rec_data")
obj=con.cursor()
class insert:
	def create_new_user(*data):
  		obj.execute("SELECT id from reject_list order by id desc limit 1")
  		ID="Q_"+str(obj.fetchone()[0]+1)
  		obj.execute("INSERT INTO reject_list (`user_id`,`time_stamp`) VALUES('%s','%s')" %(ID,data[1]))
  		con.commit()

  		return ID

	def accept_user(*data):
  		obj.execute("SELECT * from reject_list WHERE user_id='%s';" %(data[1]))
  		dat=obj.fetchone()
  		obj.execute("INSERT INTO accept_list (`user_id`) VALUES('%s')" %(data[1]))
  		con.commit()

class update:
	def update_time_stamp(*data):
		obj.execute("UPDATE accept_list SET time_stamp='%s' WHERE user_id='%s';" %(data[1],data[2]))
		con.commit()


class select:
	def select_user(*data):

		obj.execute("SELECT * FROM accept_list WHERE user_id='%s' ;" %(data[1]))
		data=obj.fetchone();
		return data

	def select_waiting_list(*data):

		obj.execute("SELECT *from reject_list ")
		data=obj.fetchall();
		return data


if __name__=="__main__":
	select=select()
	insert=insert()
	update=update()