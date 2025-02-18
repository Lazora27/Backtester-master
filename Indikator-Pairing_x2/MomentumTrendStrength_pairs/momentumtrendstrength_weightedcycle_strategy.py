import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'WeightedCycle': 1.0
        })
    )
