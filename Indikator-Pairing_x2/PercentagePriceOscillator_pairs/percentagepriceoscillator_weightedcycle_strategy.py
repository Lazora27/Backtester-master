import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'WeightedCycle': 1.0
        })
    )
