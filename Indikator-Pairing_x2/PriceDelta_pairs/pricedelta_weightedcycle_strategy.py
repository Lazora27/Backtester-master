import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'WeightedCycle': 1.0
        })
    )
