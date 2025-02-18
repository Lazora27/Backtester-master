import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und VWAPBands
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'VWAPBands': 1.0
        })
    )
