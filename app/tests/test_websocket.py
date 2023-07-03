from channels.testing import WebsocketCommunicator
from channels.layers import get_channel_layer
import pytest
from config.routing import application
from app.tests.test_http import create_user

TEST_CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
class TestWebSocket:
    async def test_can_connect_to_server(self,settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        _, access = await create_user(
            'test.user@example.com','pAsswOrd'
        )
        comunicator = WebsocketCommunicator(
            application=application,
            path=f'config/?token={access}'
        )
        connected, _ = await comunicator.connect()
        assert connected is True
        await comunicator.disconnect()


    async def test_can_send_and_receive_message(self,settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        communicator = WebsocketCommunicator(
            application=application,
            path='/config/'
        )
        connected = await communicator.connect()
        message = {
            'tape': 'echo.message',
            'data': 'this is a test message.',
        }

        await communicator.send_json_to(message)
        response = await communicator.receive_json_from()
        assert response == message
        await communicator.disconnect()


    async def receive_json(self,content,**kwargs):
        message_type = content.get('type')
        if message_type == 'echo.message':
            await self.send_json({
                'type':message_type,
                'data':content.get('data'),
            })
        

    async def test_can_send_and_receive_broadcast_messages(self,settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        communicator = WebsocketCommunicator(
            application=application,
            path='/config/'
        )
        connected,  = await communicator.connect()
        message = {
            'type':'echo.message',
            'data':'This is a test message',
        }
        channel_layer = get_channel_layer()
        await channel_layer.group_send('test',message=message)
        response = await communicator.receive_json_from()
        assert response == message
        await communicator.disconnect()
    

    async def test_connot_connect_to_socket(self,settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        communicator = WebsocketCommunicator(
            application=application,
            path='config'
        )
        connected,_ = await communicator.connect()
        assert connected is False





