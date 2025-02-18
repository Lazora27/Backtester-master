import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und DOMDepth
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'DOMDepth': 1.0
        })
    )
