import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'WeightedCycle': 1.0
        })
    )
