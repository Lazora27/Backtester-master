import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
