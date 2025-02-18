import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und DOMDepth
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'DOMDepth': 1.0
        })
    )
