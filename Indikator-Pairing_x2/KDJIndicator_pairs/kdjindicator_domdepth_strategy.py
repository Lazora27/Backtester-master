import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und DOMDepth
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'DOMDepth': 1.0
        })
    )
