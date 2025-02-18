import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
