import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'SmoothedCycle': 1.0
        })
    )
