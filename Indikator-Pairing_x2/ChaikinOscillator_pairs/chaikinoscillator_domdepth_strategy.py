import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und DOMDepth
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'DOMDepth': 1.0
        })
    )
