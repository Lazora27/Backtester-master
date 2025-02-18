import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'AverageLogRange': 1.0
        })
    )
