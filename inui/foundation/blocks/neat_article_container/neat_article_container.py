from inui.elements import *
from inui.svg import *
Html(

    data = (
        Body(

            data = (
                Div(
                    classs='''neat-article-container''',
                    data = (
                        Div(
                            classs='''row large-8 columns align-center''',
                            data = (
                                Div(
                                    classs='''neat-article-header''',
                                    data = (
                                        Div(
                                            classs='''article-header-avatar''',
                                            data = (
                                                Img(
                                                    classs='''header-avatar''',
                                                    src='''https://i.imgur.com/3AeQRbR.jpg''',
                                                ), )
                                        ), 
                                        Div(
                                            classs='''article-header-author''',
                                            data = (
                                                P(
                                                    classs='''author-name''',
                                                    data = ('''
          Harry Manchanda
        ''',)
                                                ), 
                                                P(
                                                    classs='''author-description''',
                                                    data = ('''
          Front End Developer crawling his way to Full Stack Development. Team Member @ZURB/Yetinauts!
        ''',)
                                                ), 
                                                P(
                                                    classs='''article-date-read''',
                                                    data = ('''27 April, 2017 - 5 min read''',)
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''neat-article-title''',
                                    data = (
                                        H3(
                                            classs='''article-title''',
                                            data = ('''
        Familiarity Bias is Holding You Back: It’s Time to Embrace Arrow Functions
      ''',)
                                        ), )
                                ), )
                        ), 
                        Div(
                            classs='''neat-article-image''',
                            data = (
                                Img(
                                    classs='''article-image''',
                                    src='''https://i.imgur.com/0buQ75a.jpg''',
                                    alt='''Space''',
                                ), )
                        ), 
                        Div(
                            classs='''row neat-article-content''',
                            data = (
                                Div(
                                    classs='''small-2 large-2 columns''',
                                    data_sticky_container='',
                                    data = (
                                        Div(
                                            classs='''sticky article-social''',
                                            data_sticky='',
                                            data_anchor='''sticky1''',
                                            data_sticky_on='''small''',
                                            data = (
                                                Div(
                                                    classs='''rounded-social-buttons''',
                                                    data = (
                                                        A(
                                                            classs='''social-button facebook''',
                                                            href='''#''',
                                                        ), 
                                                        A(
                                                            classs='''social-button twitter''',
                                                            href='''#''',
                                                        ), 
                                                        A(
                                                            classs='''social-button google-plus''',
                                                            href='''#''',
                                                        ), )
                                                ), )
                                        ), )
                                ), 
                                Div(
                                    classs='''small-10 large-8 columns''',
                                    id='''sticky1''',
                                    data = (
                                        Div(
                                            classs='''article-content''',
                                            data = (
                                                P(

                                                    data = ('''
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate accusantium unde culpa est dolorem earum in numquam accusamus, recusandae dolorum. Aperiam nesciunt iste numquam laboriosam, asperiores explicabo impedit laborum, non, itaque quae nemo, assumenda sequi autem pariatur debitis obcaecati culpa mollitia ratione perspiciatis officiis accusamus magni! Inventore ipsam alias non ea dolores veritatis vero sint libero tempore. Alias vero, libero sapiente, maxime facilis magnam, natus modi mollitia at ut numquam consequuntur expedita recusandae incidunt perspiciatis placeat sint doloribus. Ipsam numquam, optio consequuntur commodi possimus! Earum rem rerum, possimus, quae repellat modi omnis quos sapiente magni nesciunt similique atque veniam ipsa.
        ''',)
                                                ), 
                                                P(

                                                    data = ('''
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate accusantium unde culpa est dolorem earum in numquam accusamus, recusandae dolorum. Aperiam nesciunt iste numquam laboriosam, asperiores explicabo impedit laborum, non, itaque quae nemo, assumenda sequi autem pariatur debitis obcaecati culpa mollitia ratione perspiciatis officiis accusamus magni! Inventore ipsam alias non ea dolores veritatis vero sint libero tempore. Alias vero, libero sapiente, maxime facilis magnam, natus modi mollitia at ut numquam consequuntur expedita recusandae incidunt perspiciatis placeat sint doloribus. Ipsam numquam, optio consequuntur commodi possimus! Earum rem rerum, possimus, quae repellat modi omnis quos sapiente magni nesciunt similique atque veniam ipsa.
        ''',)
                                                ), 
                                                P(

                                                    data = ('''
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate accusantium unde culpa est dolorem earum in numquam accusamus, recusandae dolorum. Aperiam nesciunt iste numquam laboriosam, asperiores explicabo impedit laborum, non, itaque quae nemo, assumenda sequi autem pariatur debitis obcaecati culpa mollitia ratione perspiciatis officiis accusamus magni! Inventore ipsam alias non ea dolores veritatis vero sint libero tempore. Alias vero, libero sapiente, maxime facilis magnam, natus modi mollitia at ut numquam consequuntur expedita recusandae incidunt perspiciatis placeat sint doloribus. Ipsam numquam, optio consequuntur commodi possimus! Earum rem rerum, possimus, quae repellat modi omnis quos sapiente magni nesciunt similique atque veniam ipsa.
        ''',)
                                                ), 
                                                P(

                                                    data = ('''
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate accusantium unde culpa est dolorem earum in numquam accusamus, recusandae dolorum. Aperiam nesciunt iste numquam laboriosam, asperiores explicabo impedit laborum, non, itaque quae nemo, assumenda sequi autem pariatur debitis obcaecati culpa mollitia ratione perspiciatis officiis accusamus magni! Inventore ipsam alias non ea dolores veritatis vero sint libero tempore. Alias vero, libero sapiente, maxime facilis magnam, natus modi mollitia at ut numquam consequuntur expedita recusandae incidunt perspiciatis placeat sint doloribus. Ipsam numquam, optio consequuntur commodi possimus! Earum rem rerum, possimus, quae repellat modi omnis quos sapiente magni nesciunt similique atque veniam ipsa.
        ''',)
                                                ), 
                                                P(

                                                    data = ('''
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate accusantium unde culpa est dolorem earum in numquam accusamus, recusandae dolorum. Aperiam nesciunt iste numquam laboriosam, asperiores explicabo impedit laborum, non, itaque quae nemo, assumenda sequi autem pariatur debitis obcaecati culpa mollitia ratione perspiciatis officiis accusamus magni! Inventore ipsam alias non ea dolores veritatis vero sint libero tempore. Alias vero, libero sapiente, maxime facilis magnam, natus modi mollitia at ut numquam consequuntur expedita recusandae incidunt perspiciatis placeat sint doloribus. Ipsam numquam, optio consequuntur commodi possimus! Earum rem rerum, possimus, quae repellat modi omnis quos sapiente magni nesciunt similique atque veniam ipsa.
        ''',)
                                                ), 
                                                P(

                                                    data = ('''
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate accusantium unde culpa est dolorem earum in numquam accusamus, recusandae dolorum. Aperiam nesciunt iste numquam laboriosam, asperiores explicabo impedit laborum, non, itaque quae nemo, assumenda sequi autem pariatur debitis obcaecati culpa mollitia ratione perspiciatis officiis accusamus magni! Inventore ipsam alias non ea dolores veritatis vero sint libero tempore. Alias vero, libero sapiente, maxime facilis magnam, natus modi mollitia at ut numquam consequuntur expedita recusandae incidunt perspiciatis placeat sint doloribus. Ipsam numquam, optio consequuntur commodi possimus! Earum rem rerum, possimus, quae repellat modi omnis quos sapiente magni nesciunt similique atque veniam ipsa.
        ''',)
                                                ), 
                                                P(

                                                    data = ('''
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate accusantium unde culpa est dolorem earum in numquam accusamus, recusandae dolorum. Aperiam nesciunt iste numquam laboriosam, asperiores explicabo impedit laborum, non, itaque quae nemo, assumenda sequi autem pariatur debitis obcaecati culpa mollitia ratione perspiciatis officiis accusamus magni! Inventore ipsam alias non ea dolores veritatis vero sint libero tempore. Alias vero, libero sapiente, maxime facilis magnam, natus modi mollitia at ut numquam consequuntur expedita recusandae incidunt perspiciatis placeat sint doloribus. Ipsam numquam, optio consequuntur commodi possimus! Earum rem rerum, possimus, quae repellat modi omnis quos sapiente magni nesciunt similique atque veniam ipsa.
        ''',)
                                                ), 
                                                P(

                                                    data = ('''
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate accusantium unde culpa est dolorem earum in numquam accusamus, recusandae dolorum. Aperiam nesciunt iste numquam laboriosam, asperiores explicabo impedit laborum, non, itaque quae nemo, assumenda sequi autem pariatur debitis obcaecati culpa mollitia ratione perspiciatis officiis accusamus magni! Inventore ipsam alias non ea dolores veritatis vero sint libero tempore. Alias vero, libero sapiente, maxime facilis magnam, natus modi mollitia at ut numquam consequuntur expedita recusandae incidunt perspiciatis placeat sint doloribus. Ipsam numquam, optio consequuntur commodi possimus! Earum rem rerum, possimus, quae repellat modi omnis quos sapiente magni nesciunt similique atque veniam ipsa.
        ''',)
                                                ), 
                                                P(

                                                    data = ('''
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptate accusantium unde culpa est dolorem earum in numquam accusamus, recusandae dolorum. Aperiam nesciunt iste numquam laboriosam, asperiores explicabo impedit laborum, non, itaque quae nemo, assumenda sequi autem pariatur debitis obcaecati culpa mollitia ratione perspiciatis officiis accusamus magni! Inventore ipsam alias non ea dolores veritatis vero sint libero tempore. Alias vero, libero sapiente, maxime facilis magnam, natus modi mollitia at ut numquam consequuntur expedita recusandae incidunt perspiciatis placeat sint doloribus. Ipsam numquam, optio consequuntur commodi possimus! Earum rem rerum, possimus, quae repellat modi omnis quos sapiente magni nesciunt similique atque veniam ipsa.
        ''',)
                                                ), )
                                        ), )
                                ), )
                        ), )
                ), )
        ), )
)