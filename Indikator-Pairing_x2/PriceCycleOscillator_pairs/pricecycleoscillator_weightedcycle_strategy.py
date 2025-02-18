import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceCycleOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceCycleOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'PriceCycleOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
