import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'WeightedCycle': 1.0
        })
    )
