import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
