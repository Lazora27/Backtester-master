import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
