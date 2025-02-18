import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'SmoothedCycle': 1.0
        })
    )
