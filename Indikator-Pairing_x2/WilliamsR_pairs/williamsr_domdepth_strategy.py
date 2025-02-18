import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und DOMDepth
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'DOMDepth': 1.0
        })
    )
