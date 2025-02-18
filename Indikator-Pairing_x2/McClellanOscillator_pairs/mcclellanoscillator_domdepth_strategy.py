import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und DOMDepth
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'DOMDepth': 1.0
        })
    )
