import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'WeightedCycle': 1.0
        })
    )
