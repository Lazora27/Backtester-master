import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'WeightedCycle': 1.0
        })
    )
