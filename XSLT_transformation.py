def xlst_get_data():
    with open('XSLT_transform/xslt_in.xml', 'r') as in_file:
        data_in = in_file.read()

        return data_in


def xlst_transform(data):


    res = data
    return res


def xlst_out(res_data):
    with open('XSLT_transform/xslt_out.xml', 'w') as out_file:
        out_file.write(res_data)


if __name__ == "__main__":
    data_in = xlst_get_data()
    data_out = xlst_transform(data_in)
    xlst_out()
