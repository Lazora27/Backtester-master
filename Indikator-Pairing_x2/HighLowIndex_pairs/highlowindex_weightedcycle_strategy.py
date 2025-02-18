import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
