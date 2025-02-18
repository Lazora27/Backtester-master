import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und DOMDepth
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'DOMDepth': 1.0
        })
    )
