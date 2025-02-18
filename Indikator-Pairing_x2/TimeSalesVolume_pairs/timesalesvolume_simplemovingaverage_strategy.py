import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
