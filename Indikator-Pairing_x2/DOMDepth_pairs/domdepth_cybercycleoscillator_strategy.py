import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
