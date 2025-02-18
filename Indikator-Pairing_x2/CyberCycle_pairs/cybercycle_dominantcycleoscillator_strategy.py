import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
