import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'WeightedCycle': 1.0
        })
    )
