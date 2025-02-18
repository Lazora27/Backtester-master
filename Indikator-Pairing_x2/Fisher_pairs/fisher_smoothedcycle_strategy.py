import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'SmoothedCycle': 1.0
        })
    )
