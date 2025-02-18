import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und DOMDepth
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'DOMDepth': 1.0
        })
    )
