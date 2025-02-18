import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
