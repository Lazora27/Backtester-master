import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'WeightedCycle': 1.0
        })
    )
