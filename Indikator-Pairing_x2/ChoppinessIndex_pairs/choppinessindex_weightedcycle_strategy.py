import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
