import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'WeightedCycle': 1.0
        })
    )
