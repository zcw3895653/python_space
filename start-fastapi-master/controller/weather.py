from service import tianqi as tianqi_service
from application.controller import success, error
from application.logger import get_controller_logger
from fastapi import APIRouter, BackgroundTasks


router = APIRouter()
LOGGER = get_controller_logger('TIANQI')


@router.get('/weather/{city_id}')
async def get_tianqi(city_id: str):
            LOGGER.info('Get tianqi with id: %s' % city_id)
            tianqi = tianqi_service.get_tianqi(city_id)
            if not tianqi:
                return error(msg='Cannot found item with id %s' % city_id)
            return success(tianqi)

@router.post('/weather/')
async def get_tianqi(city_id: str):
            LOGGER.info('Get tianqi with id: %s' % city_id)
            tianqi = tianqi_service.get_tianqi(city_id)
            if not tianqi:
                return error(msg='Cannot found item with id %s' % city_id)
            return success(tianqi)

@router.post('/weather/forecast')
async def get_tianqi(city_id: str):
            LOGGER.info('Get tianqi with id: %s' % city_id)
            tianqi = tianqi_service.get_tianqi(city_id)
            if not tianqi:
                return error(msg='Cannot found item with id %s' % city_id)
            return success(tianqi)

@router.post('/air/now')
async def get_tianqi(city_id: str):
            LOGGER.info('Get tianqi with id: %s' % city_id)
            tianqi = tianqi_service.get_tianqi(city_id)
            if not tianqi:
                return error(msg='Cannot found item with id %s' % city_id)
            return success(tianqi)