import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'SmoothedCycle': 1.0
        })
    )
