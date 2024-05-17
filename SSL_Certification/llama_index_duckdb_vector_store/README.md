# Introduction
- https://docs.llamaindex.ai/en/stable/examples/vector_stores/DuckDBDemo/

```python
# code part that gives error
vector_store = DuckDBVectorStore(embed_dim=512, persist_dir="./persist/")
```

**Full code**
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.duckdb import DuckDBVectorStore
from llama_index.core import StorageContext

from IPython.display import Markdown, display
import duckdb
import os
import openai
import llama_index
import llama_index.vector_stores.duckdb
%load_ext watermark

#========= settings
import os,sys
sys.path.append(os.path.expanduser("~/.utils"))
from util_openai import openai_api_key, azure_endpoint,openai_api_version
api_key = openai_api_key
api_version = "2023-03-15-preview"

# os environ
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["OPENAI_API_TYPE"] = 'azure'
os.environ["OPENAI_API_VERSION"] = api_version
os.environ['AZURE_OPENAI_ENDPOINT'] = azure_endpoint

# openai keys
openai.api_key = openai_api_key
openai.api_type = 'azure'
openai.api_version = api_version
openai.azure_endpoint = azure_endpoint

import os

# Create the directory if it does not exist
os.makedirs('data/paul_graham/', exist_ok=True)

import requests

url = 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt'
file_path = 'data/paul_graham/paul_graham_essay.txt'

response = requests.get(url,verify=False)
if response.status_code == 200:
    with open(file_path, 'wb') as file:
        file.write(response.content)
        print("File downloaded successfully.")
else:
    print("Failed to download the file.")


documents = SimpleDirectoryReader("data/paul_graham/").load_data()
vector_store = DuckDBVectorStore(embed_dim=512, persist_dir="./persist/")
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
display(Markdown(f"{response}"))
```

# Error
```bash
Retrying llama_index.embeddings.openai.base.get_embeddings in 0.32245356053578966 seconds as it raised APIConnectionError: Connection error..
---------------------------------------------------------------------------
ConnectError                              Traceback (most recent call last)
File ~\venv\py312_llama_index\Lib\site-packages\httpx\_transports\default.py:69, in map_httpcore_exceptions()
     68 try:
---> 69     yield
     70 except Exception as exc:

File ~\venv\py312_llama_index\Lib\site-packages\httpx\_transports\default.py:233, in HTTPTransport.handle_request(self, request)
    232 with map_httpcore_exceptions():
--> 233     resp = self._pool.handle_request(req)
    235 assert isinstance(resp.stream, typing.Iterable)

File ~\venv\py312_llama_index\Lib\site-packages\httpcore\_sync\connection_pool.py:216, in ConnectionPool.handle_request(self, request)
    215     self._close_connections(closing)
--> 216     raise exc from None
    218 # Return the response. Note that in this case we still have to manage
    219 # the point at which the response is closed.

File ~\venv\py312_llama_index\Lib\site-packages\httpcore\_sync\connection_pool.py:196, in ConnectionPool.handle_request(self, request)
    194 try:
    195     # Send the request on the assigned connection.
--> 196     response = connection.handle_request(
    197         pool_request.request
    198     )
    199 except ConnectionNotAvailable:
    200     # In some cases a connection may initially be available to
    201     # handle a request, but then become unavailable.
    202     #
    203     # In this case we clear the connection and try again.

File ~\venv\py312_llama_index\Lib\site-packages\httpcore\_sync\connection.py:99, in HTTPConnection.handle_request(self, request)
     98     self._connect_failed = True
---> 99     raise exc
    101 return self._connection.handle_request(request)

File ~\venv\py312_llama_index\Lib\site-packages\httpcore\_sync\connection.py:76, in HTTPConnection.handle_request(self, request)
     75 if self._connection is None:
---> 76     stream = self._connect(request)
     78     ssl_object = stream.get_extra_info("ssl_object")

File ~\venv\py312_llama_index\Lib\site-packages\httpcore\_sync\connection.py:154, in HTTPConnection._connect(self, request)
    153 with Trace("start_tls", logger, request, kwargs) as trace:
--> 154     stream = stream.start_tls(**kwargs)
    155     trace.return_value = stream

File ~\venv\py312_llama_index\Lib\site-packages\httpcore\_backends\sync.py:152, in SyncStream.start_tls(self, ssl_context, server_hostname, timeout)
    148 exc_map: ExceptionMapping = {
    149     socket.timeout: ConnectTimeout,
    150     OSError: ConnectError,
    151 }
--> 152 with map_exceptions(exc_map):
    153     try:

File ~\AppData\Local\Programs\Python\Python312\Lib\contextlib.py:158, in _GeneratorContextManager.__exit__(self, typ, value, traceback)
    157 try:
--> 158     self.gen.throw(value)
    159 except StopIteration as exc:
    160     # Suppress StopIteration *unless* it's the same exception that
    161     # was passed to throw().  This prevents a StopIteration
    162     # raised inside the "with" statement from being suppressed.

File ~\venv\py312_llama_index\Lib\site-packages\httpcore\_exceptions.py:14, in map_exceptions(map)
     13     if isinstance(exc, from_exc):
---> 14         raise to_exc(exc) from exc
     15 raise

ConnectError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1000)

The above exception was the direct cause of the following exception:

ConnectError                              Traceback (most recent call last)
File ~\venv\py312_llama_index\Lib\site-packages\openai\_base_client.py:952, in SyncAPIClient._request(self, cast_to, options, remaining_retries, stream, stream_cls)
    951 try:
--> 952     response = self._client.send(
    953         request,
    954         stream=stream or self._should_stream_response_body(request=request),
    955         **kwargs,
    956     )
    957 except httpx.TimeoutException as err:

File ~\venv\py312_llama_index\Lib\site-packages\httpx\_client.py:914, in Client.send(self, request, stream, auth, follow_redirects)
    912 auth = self._build_request_auth(request, auth)
--> 914 response = self._send_handling_auth(
    915     request,
    916     auth=auth,
    917     follow_redirects=follow_redirects,
    918     history=[],
    919 )
    920 try:

File ~\venv\py312_llama_index\Lib\site-packages\httpx\_client.py:942, in Client._send_handling_auth(self, request, auth, follow_redirects, history)
    941 while True:
--> 942     response = self._send_handling_redirects(
    943         request,
    944         follow_redirects=follow_redirects,
    945         history=history,
    946     )
    947     try:

File ~\venv\py312_llama_index\Lib\site-packages\httpx\_client.py:979, in Client._send_handling_redirects(self, request, follow_redirects, history)
    977     hook(request)
--> 979 response = self._send_single_request(request)
    980 try:

File ~\venv\py312_llama_index\Lib\site-packages\httpx\_client.py:1015, in Client._send_single_request(self, request)
   1014 with request_context(request=request):
-> 1015     response = transport.handle_request(request)
   1017 assert isinstance(response.stream, SyncByteStream)

File ~\venv\py312_llama_index\Lib\site-packages\httpx\_transports\default.py:232, in HTTPTransport.handle_request(self, request)
    220 req = httpcore.Request(
    221     method=request.method,
    222     url=httpcore.URL(
   (...)
    230     extensions=request.extensions,
    231 )
--> 232 with map_httpcore_exceptions():
    233     resp = self._pool.handle_request(req)

File ~\AppData\Local\Programs\Python\Python312\Lib\contextlib.py:158, in _GeneratorContextManager.__exit__(self, typ, value, traceback)
    157 try:
--> 158     self.gen.throw(value)
    159 except StopIteration as exc:
    160     # Suppress StopIteration *unless* it's the same exception that
    161     # was passed to throw().  This prevents a StopIteration
    162     # raised inside the "with" statement from being suppressed.

File ~\venv\py312_llama_index\Lib\site-packages\httpx\_transports\default.py:86, in map_httpcore_exceptions()
     85 message = str(exc)
---> 86 raise mapped_exc(message) from exc

ConnectError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1000)

The above exception was the direct cause of the following exception:

APIConnectionError                        Traceback (most recent call last)
Cell In[14], line 11
      8 vector_store = DuckDBVectorStore(embed_dim=512, persist_dir="./persist/")
      9 storage_context = StorageContext.from_defaults(vector_store=vector_store)
---> 11 index = VectorStoreIndex.from_documents(
     12     documents, storage_context=storage_context
     13 )

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\core\indices\base.py:145, in BaseIndex.from_documents(cls, documents, storage_context, show_progress, callback_manager, transformations, service_context, **kwargs)
    136     docstore.set_document_hash(doc.get_doc_id(), doc.hash)
    138 nodes = run_transformations(
    139     documents,  # type: ignore
    140     transformations,
    141     show_progress=show_progress,
    142     **kwargs,
    143 )
--> 145 return cls(
    146     nodes=nodes,
    147     storage_context=storage_context,
    148     callback_manager=callback_manager,
    149     show_progress=show_progress,
    150     transformations=transformations,
    151     service_context=service_context,
    152     **kwargs,
    153 )

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\core\indices\vector_store\base.py:75, in VectorStoreIndex.__init__(self, nodes, use_async, store_nodes_override, embed_model, insert_batch_size, objects, index_struct, storage_context, callback_manager, transformations, show_progress, service_context, **kwargs)
     68 self._embed_model = (
     69     resolve_embed_model(embed_model, callback_manager=callback_manager)
     70     if embed_model
     71     else embed_model_from_settings_or_context(Settings, service_context)
     72 )
     74 self._insert_batch_size = insert_batch_size
---> 75 super().__init__(
     76     nodes=nodes,
     77     index_struct=index_struct,
     78     service_context=service_context,
     79     storage_context=storage_context,
     80     show_progress=show_progress,
     81     objects=objects,
     82     callback_manager=callback_manager,
     83     transformations=transformations,
     84     **kwargs,
     85 )

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\core\indices\base.py:94, in BaseIndex.__init__(self, nodes, objects, index_struct, storage_context, callback_manager, transformations, show_progress, service_context, **kwargs)
     92 if index_struct is None:
     93     nodes = nodes or []
---> 94     index_struct = self.build_index_from_nodes(
     95         nodes + objects  # type: ignore
     96     )
     97 self._index_struct = index_struct
     98 self._storage_context.index_store.add_index_struct(self._index_struct)

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\core\indices\vector_store\base.py:308, in VectorStoreIndex.build_index_from_nodes(self, nodes, **insert_kwargs)
    300 if any(
    301     node.get_content(metadata_mode=MetadataMode.EMBED) == "" for node in nodes
    302 ):
    303     raise ValueError(
    304         "Cannot build index from nodes with no content. "
    305         "Please ensure all nodes have content."
    306     )
--> 308 return self._build_index_from_nodes(nodes, **insert_kwargs)

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\core\indices\vector_store\base.py:280, in VectorStoreIndex._build_index_from_nodes(self, nodes, **insert_kwargs)
    278     run_async_tasks(tasks)
    279 else:
--> 280     self._add_nodes_to_index(
    281         index_struct,
    282         nodes,
    283         show_progress=self._show_progress,
    284         **insert_kwargs,
    285     )
    286 return index_struct

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\core\indices\vector_store\base.py:233, in VectorStoreIndex._add_nodes_to_index(self, index_struct, nodes, show_progress, **insert_kwargs)
    230     return
    232 for nodes_batch in iter_batch(nodes, self._insert_batch_size):
--> 233     nodes_batch = self._get_node_with_embedding(nodes_batch, show_progress)
    234     new_ids = self._vector_store.add(nodes_batch, **insert_kwargs)
    236     if not self._vector_store.stores_text or self._store_nodes_override:
    237         # NOTE: if the vector store doesn't store text,
    238         # we need to add the nodes to the index struct and document store

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\core\indices\vector_store\base.py:141, in VectorStoreIndex._get_node_with_embedding(self, nodes, show_progress)
    130 def _get_node_with_embedding(
    131     self,
    132     nodes: Sequence[BaseNode],
    133     show_progress: bool = False,
    134 ) -> List[BaseNode]:
    135     """Get tuples of id, node, and embedding.
    136 
    137     Allows us to store these nodes in a vector store.
    138     Embeddings are called in batches.
    139 
    140     """
--> 141     id_to_embed_map = embed_nodes(
    142         nodes, self._embed_model, show_progress=show_progress
    143     )
    145     results = []
    146     for node in nodes:

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\core\indices\utils.py:138, in embed_nodes(nodes, embed_model, show_progress)
    135     else:
    136         id_to_embed_map[node.node_id] = node.embedding
--> 138 new_embeddings = embed_model.get_text_embedding_batch(
    139     texts_to_embed, show_progress=show_progress
    140 )
    142 for new_id, text_embedding in zip(ids_to_embed, new_embeddings):
    143     id_to_embed_map[new_id] = text_embedding

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\core\instrumentation\dispatcher.py:274, in Dispatcher.span.<locals>.wrapper(func, instance, args, kwargs)
    270 self.span_enter(
    271     id_=id_, bound_args=bound_args, instance=instance, parent_id=parent_id
    272 )
    273 try:
--> 274     result = func(*args, **kwargs)
    275 except BaseException as e:
    276     self.event(SpanDropEvent(span_id=id_, err_str=str(e)))

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\core\base\embeddings\base.py:341, in BaseEmbedding.get_text_embedding_batch(self, texts, show_progress, **kwargs)
    332 dispatch_event(
    333     EmbeddingStartEvent(
    334         model_dict=model_dict,
    335     )
    336 )
    337 with self.callback_manager.event(
    338     CBEventType.EMBEDDING,
    339     payload={EventPayload.SERIALIZED: self.to_dict()},
    340 ) as event:
--> 341     embeddings = self._get_text_embeddings(cur_batch)
    342     result_embeddings.extend(embeddings)
    343     event.on_end(
    344         payload={
    345             EventPayload.CHUNKS: cur_batch,
    346             EventPayload.EMBEDDINGS: embeddings,
    347         },
    348     )

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\embeddings\openai\base.py:429, in OpenAIEmbedding._get_text_embeddings(self, texts)
    422 """Get text embeddings.
    423 
    424 By default, this is a wrapper around _get_text_embedding.
    425 Can be overridden for batch queries.
    426 
    427 """
    428 client = self._get_client()
--> 429 return get_embeddings(
    430     client,
    431     texts,
    432     engine=self._text_engine,
    433     **self.additional_kwargs,
    434 )

File ~\venv\py312_llama_index\Lib\site-packages\tenacity\__init__.py:330, in BaseRetrying.wraps.<locals>.wrapped_f(*args, **kw)
    326 @functools.wraps(
    327     f, functools.WRAPPER_ASSIGNMENTS + ("__defaults__", "__kwdefaults__")
    328 )
    329 def wrapped_f(*args: t.Any, **kw: t.Any) -> t.Any:
--> 330     return self(f, *args, **kw)

File ~\venv\py312_llama_index\Lib\site-packages\tenacity\__init__.py:467, in Retrying.__call__(self, fn, *args, **kwargs)
    465 retry_state = RetryCallState(retry_object=self, fn=fn, args=args, kwargs=kwargs)
    466 while True:
--> 467     do = self.iter(retry_state=retry_state)
    468     if isinstance(do, DoAttempt):
    469         try:

File ~\venv\py312_llama_index\Lib\site-packages\tenacity\__init__.py:368, in BaseRetrying.iter(self, retry_state)
    366 result = None
    367 for action in self.iter_state.actions:
--> 368     result = action(retry_state)
    369 return result

File ~\venv\py312_llama_index\Lib\site-packages\tenacity\__init__.py:410, in BaseRetrying._post_stop_check_actions.<locals>.exc_check(rs)
    408 retry_exc = self.retry_error_cls(fut)
    409 if self.reraise:
--> 410     raise retry_exc.reraise()
    411 raise retry_exc from fut.exception()

File ~\venv\py312_llama_index\Lib\site-packages\tenacity\__init__.py:183, in RetryError.reraise(self)
    181 def reraise(self) -> t.NoReturn:
    182     if self.last_attempt.failed:
--> 183         raise self.last_attempt.result()
    184     raise self

File ~\AppData\Local\Programs\Python\Python312\Lib\concurrent\futures\_base.py:449, in Future.result(self, timeout)
    447     raise CancelledError()
    448 elif self._state == FINISHED:
--> 449     return self.__get_result()
    451 self._condition.wait(timeout)
    453 if self._state in [CANCELLED, CANCELLED_AND_NOTIFIED]:

File ~\AppData\Local\Programs\Python\Python312\Lib\concurrent\futures\_base.py:401, in Future.__get_result(self)
    399 if self._exception:
    400     try:
--> 401         raise self._exception
    402     finally:
    403         # Break a reference cycle with the exception in self._exception
    404         self = None

File ~\venv\py312_llama_index\Lib\site-packages\tenacity\__init__.py:470, in Retrying.__call__(self, fn, *args, **kwargs)
    468 if isinstance(do, DoAttempt):
    469     try:
--> 470         result = fn(*args, **kwargs)
    471     except BaseException:  # noqa: B902
    472         retry_state.set_exception(sys.exc_info())  # type: ignore[arg-type]

File ~\venv\py312_llama_index\Lib\site-packages\llama_index\embeddings\openai\base.py:180, in get_embeddings(client, list_of_text, engine, **kwargs)
    176 assert len(list_of_text) <= 2048, "The batch size should not be larger than 2048."
    178 list_of_text = [text.replace("\n", " ") for text in list_of_text]
--> 180 data = client.embeddings.create(input=list_of_text, model=engine, **kwargs).data
    181 return [d.embedding for d in data]

File ~\venv\py312_llama_index\Lib\site-packages\openai\resources\embeddings.py:114, in Embeddings.create(self, input, model, dimensions, encoding_format, user, extra_headers, extra_query, extra_body, timeout)
    108         embedding.embedding = np.frombuffer(  # type: ignore[no-untyped-call]
    109             base64.b64decode(data), dtype="float32"
    110         ).tolist()
    112     return obj
--> 114 return self._post(
    115     "/embeddings",
    116     body=maybe_transform(params, embedding_create_params.EmbeddingCreateParams),
    117     options=make_request_options(
    118         extra_headers=extra_headers,
    119         extra_query=extra_query,
    120         extra_body=extra_body,
    121         timeout=timeout,
    122         post_parser=parser,
    123     ),
    124     cast_to=CreateEmbeddingResponse,
    125 )

File ~\venv\py312_llama_index\Lib\site-packages\openai\_base_client.py:1240, in SyncAPIClient.post(self, path, cast_to, body, options, files, stream, stream_cls)
   1226 def post(
   1227     self,
   1228     path: str,
   (...)
   1235     stream_cls: type[_StreamT] | None = None,
   1236 ) -> ResponseT | _StreamT:
   1237     opts = FinalRequestOptions.construct(
   1238         method="post", url=path, json_data=body, files=to_httpx_files(files), **options
   1239     )
-> 1240     return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))

File ~\venv\py312_llama_index\Lib\site-packages\openai\_base_client.py:921, in SyncAPIClient.request(self, cast_to, options, remaining_retries, stream, stream_cls)
    912 def request(
    913     self,
    914     cast_to: Type[ResponseT],
   (...)
    919     stream_cls: type[_StreamT] | None = None,
    920 ) -> ResponseT | _StreamT:
--> 921     return self._request(
    922         cast_to=cast_to,
    923         options=options,
    924         stream=stream,
    925         stream_cls=stream_cls,
    926         remaining_retries=remaining_retries,
    927     )

File ~\venv\py312_llama_index\Lib\site-packages\openai\_base_client.py:976, in SyncAPIClient._request(self, cast_to, options, remaining_retries, stream, stream_cls)
    973 log.debug("Encountered Exception", exc_info=True)
    975 if retries > 0:
--> 976     return self._retry_request(
    977         options,
    978         cast_to,
    979         retries,
    980         stream=stream,
    981         stream_cls=stream_cls,
    982         response_headers=None,
    983     )
    985 log.debug("Raising connection error")
    986 raise APIConnectionError(request=request) from err

File ~\venv\py312_llama_index\Lib\site-packages\openai\_base_client.py:1053, in SyncAPIClient._retry_request(self, options, cast_to, remaining_retries, response_headers, stream, stream_cls)
   1049 # In a synchronous context we are blocking the entire thread. Up to the library user to run the client in a
   1050 # different thread if necessary.
   1051 time.sleep(timeout)
-> 1053 return self._request(
   1054     options=options,
   1055     cast_to=cast_to,
   1056     remaining_retries=remaining,
   1057     stream=stream,
   1058     stream_cls=stream_cls,
   1059 )

File ~\venv\py312_llama_index\Lib\site-packages\openai\_base_client.py:976, in SyncAPIClient._request(self, cast_to, options, remaining_retries, stream, stream_cls)
    973 log.debug("Encountered Exception", exc_info=True)
    975 if retries > 0:
--> 976     return self._retry_request(
    977         options,
    978         cast_to,
    979         retries,
    980         stream=stream,
    981         stream_cls=stream_cls,
    982         response_headers=None,
    983     )
    985 log.debug("Raising connection error")
    986 raise APIConnectionError(request=request) from err

File ~\venv\py312_llama_index\Lib\site-packages\openai\_base_client.py:1053, in SyncAPIClient._retry_request(self, options, cast_to, remaining_retries, response_headers, stream, stream_cls)
   1049 # In a synchronous context we are blocking the entire thread. Up to the library user to run the client in a
   1050 # different thread if necessary.
   1051 time.sleep(timeout)
-> 1053 return self._request(
   1054     options=options,
   1055     cast_to=cast_to,
   1056     remaining_retries=remaining,
   1057     stream=stream,
   1058     stream_cls=stream_cls,
   1059 )

    [... skipping similar frames: SyncAPIClient._request at line 976 (7 times), SyncAPIClient._retry_request at line 1053 (7 times)]

File ~\venv\py312_llama_index\Lib\site-packages\openai\_base_client.py:976, in SyncAPIClient._request(self, cast_to, options, remaining_retries, stream, stream_cls)
    973 log.debug("Encountered Exception", exc_info=True)
    975 if retries > 0:
--> 976     return self._retry_request(
    977         options,
    978         cast_to,
    979         retries,
    980         stream=stream,
    981         stream_cls=stream_cls,
    982         response_headers=None,
    983     )
    985 log.debug("Raising connection error")
    986 raise APIConnectionError(request=request) from err

File ~\venv\py312_llama_index\Lib\site-packages\openai\_base_client.py:1053, in SyncAPIClient._retry_request(self, options, cast_to, remaining_retries, response_headers, stream, stream_cls)
   1049 # In a synchronous context we are blocking the entire thread. Up to the library user to run the client in a
   1050 # different thread if necessary.
   1051 time.sleep(timeout)
-> 1053 return self._request(
   1054     options=options,
   1055     cast_to=cast_to,
   1056     remaining_retries=remaining,
   1057     stream=stream,
   1058     stream_cls=stream_cls,
   1059 )

File ~\venv\py312_llama_index\Lib\site-packages\openai\_base_client.py:986, in SyncAPIClient._request(self, cast_to, options, remaining_retries, stream, stream_cls)
    976         return self._retry_request(
    977             options,
    978             cast_to,
   (...)
    982             response_headers=None,
    983         )
    985     log.debug("Raising connection error")
--> 986     raise APIConnectionError(request=request) from err
    988 log.debug(
    989     'HTTP Response: %s %s "%i %s" %s',
    990     request.method,
   (...)
    994     response.headers,
    995 )
    996 log.debug("request_id: %s", response.headers.get("x-request-id"))

APIConnectionError: Connection error.
```
