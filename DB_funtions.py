import MySQLdb
con=MySQLdb.connect("localhost","root","test","face_rec_data")
obj=con.cursor()
class insert:
	def create_new_user(*data):
  		obj.execute("SELECT id from wait_list order by id desc limit 1")
  		ID="wid_"+str(obj.fetchone()[0]+1)
  		obj.execute("INSERT INTO wait_list (`user_id`,`time_stamp`) VALUES('%s','%s')" %(ID,data[1]))
  		con.commit()

  		return ID

	def accept_user(*data):
		print(data[1])
		obj.execute("DELETE  FROM wait_list WHERE id='%s' ;" %(data[1]))
		con.commit()
		obj.execute("SELECT id from accept_list order by id desc limit 1")
		id="id_"+str(obj.fetchone()[0]+1)
		obj.execute(" INSERT INTO accept_list (`user_id`) VALUES('%s')" %(id))
		con.commit()
		return id
	def reject_user(*data):
		print(data[1])
		obj.execute("DELETE  FROM wait_list WHERE user_id='%s' ;" %('wid_'+data[1]))
		con.commit()
		obj.execute("SELECT id from reject_list order by id desc limit 1")
		id="rjtd_"+str(obj.fetchone()[0]+1)
		obj.execute("INSERT INTO reject_list (`user_id`) VALUES('%s')" %(id))
		con.commit()
		return id

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

		obj.execute("SELECT * from wait_list WHERE id!='%s' ;" %(1))
		data=obj.fetchall();
		return data

class delete:
	def del_reject_list(*data):
		# print(data[0])
		obj.execute("DELETE  FROM reject_list WHERE user_id='%s' ;" %(data[0]))
		con.commit()


if __name__=="__main__":
	select=select()
	insert=insert()
	update=update()