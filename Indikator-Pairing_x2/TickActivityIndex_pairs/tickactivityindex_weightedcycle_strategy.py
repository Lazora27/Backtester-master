import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
