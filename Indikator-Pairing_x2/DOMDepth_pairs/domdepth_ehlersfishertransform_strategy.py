import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
