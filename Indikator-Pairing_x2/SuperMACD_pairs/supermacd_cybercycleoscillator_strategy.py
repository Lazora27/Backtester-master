import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
