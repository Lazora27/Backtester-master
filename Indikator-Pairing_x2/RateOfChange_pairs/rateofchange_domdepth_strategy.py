import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und DOMDepth
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'DOMDepth': 1.0
        })
    )
