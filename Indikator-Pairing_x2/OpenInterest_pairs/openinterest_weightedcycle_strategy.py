import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'WeightedCycle': 1.0
        })
    )
