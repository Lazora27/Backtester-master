import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
