__author__ = 'gmena'
from django.views.generic import CreateView
from helper.ImgHelper import get_valid_img


class New(CreateView):
    def form_valid(self, form):
        # Handle Image
        # Get a valid image from self.request.FILES
        img = get_valid_img('uploaded_image', self)
        if img is not None:
            if img is False:
                return self.render_to_response({
                    'error': 'Invalid Image',
                    'form': form
                })

            # Resize Image
            the_new_dir = 'my/new/dir/thumb/'

            # Set output dir
            img.set_output_dir(the_new_dir)

            # Make thumb
            # Return a string directory "my/new/dir/thumb/{the_image_named}.{format}"
            thumb = img.thumb_create(width=60, height=60)

            # Save in db?
            # model = MyDbModel()
            # model.my_pic = thumb
            # model.save()
