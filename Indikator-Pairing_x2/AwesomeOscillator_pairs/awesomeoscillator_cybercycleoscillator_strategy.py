import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
