import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'SmoothedCycle': 1.0
        })
    )
