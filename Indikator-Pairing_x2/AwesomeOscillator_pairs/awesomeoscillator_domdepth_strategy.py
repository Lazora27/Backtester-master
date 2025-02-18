import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und DOMDepth
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'DOMDepth': 1.0
        })
    )
