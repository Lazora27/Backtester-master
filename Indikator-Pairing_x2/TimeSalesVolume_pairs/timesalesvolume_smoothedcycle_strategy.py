import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'SmoothedCycle': 1.0
        })
    )
