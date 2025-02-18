import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
