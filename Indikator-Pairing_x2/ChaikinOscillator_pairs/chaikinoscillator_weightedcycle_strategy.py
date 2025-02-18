import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
