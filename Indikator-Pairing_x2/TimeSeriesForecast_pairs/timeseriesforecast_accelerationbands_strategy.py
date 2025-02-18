import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'AccelerationBands': 1.0
        })
    )
