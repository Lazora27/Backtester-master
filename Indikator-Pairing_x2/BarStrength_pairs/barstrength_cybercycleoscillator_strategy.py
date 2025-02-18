import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
