import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
