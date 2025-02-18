import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
