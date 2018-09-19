import MySQLdb
con=MySQLdb.connect("localhost","root","","face_rec_data")
obj=con.cursor()
class insert:
	def create_new_user(*data):
  		obj.execute("SELECT id from user_info order by id desc limit 1")
  		ID=obj.fetchone()[0]
  		obj.execute("INSERT INTO user_info (`user_id`,`time_stamp`) VALUES('%s','%s')" %(ID,data[1]))
  		con.commit()

  		return ID

class update:
	def update_time_stamp(*data):
		obj.execute("UPDATE user_info SET time_stamp='%s' WHERE user_id='%s';" %(data[1],data[2]))
		con.commit()


class select:
	def select_user(*data):

		obj.execute("SELECT * FROM user_info WHERE user_id='%s' ;" %(data[1]))
		data=obj.fetchone();
		return data


if __name__=="__main__":
	select=select()
	insert=insert()
	update=update()