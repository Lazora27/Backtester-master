import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendCycles_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendCycles und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TrendCycles': 1.0,
            'WeightedCycle': 1.0
        })
    )
