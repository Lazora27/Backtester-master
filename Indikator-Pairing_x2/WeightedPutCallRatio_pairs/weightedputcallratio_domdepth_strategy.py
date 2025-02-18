import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und DOMDepth
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'DOMDepth': 1.0
        })
    )
