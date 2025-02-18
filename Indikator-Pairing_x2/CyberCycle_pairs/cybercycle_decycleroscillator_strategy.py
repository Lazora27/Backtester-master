import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
