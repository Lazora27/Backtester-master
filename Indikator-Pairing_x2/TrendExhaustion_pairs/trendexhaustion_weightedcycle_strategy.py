import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'WeightedCycle': 1.0
        })
    )
