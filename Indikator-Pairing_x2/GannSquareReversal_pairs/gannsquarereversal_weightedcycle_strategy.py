import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'WeightedCycle': 1.0
        })
    )
