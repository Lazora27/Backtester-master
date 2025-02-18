import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und MovingAverage
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'MovingAverage': 1.0
        })
    )
