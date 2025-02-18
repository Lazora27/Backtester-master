import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
