from pkg_resources import resource_stream, resource_filename
import pathlib

resource_path = resource_filename('odifmap', 'resources')
# force POSIX-style path, even on Windows
resource_path = pathlib.Path(resource_path).as_posix()

lung_ontology = resource_stream('odifmap.resources', 'lung_ontology.owl')