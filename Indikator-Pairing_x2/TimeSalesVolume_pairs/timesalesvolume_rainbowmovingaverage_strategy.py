import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
