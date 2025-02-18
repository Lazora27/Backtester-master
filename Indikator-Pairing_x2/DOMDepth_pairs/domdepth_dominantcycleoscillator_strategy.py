import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
