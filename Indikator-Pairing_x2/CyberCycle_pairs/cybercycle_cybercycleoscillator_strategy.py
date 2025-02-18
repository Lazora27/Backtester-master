import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
