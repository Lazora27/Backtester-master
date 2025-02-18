import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ExtensionProjections': 1.0
        })
    )
