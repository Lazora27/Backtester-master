import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycleOscillator_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycleOscillator und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'CyberCycleOscillator': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
