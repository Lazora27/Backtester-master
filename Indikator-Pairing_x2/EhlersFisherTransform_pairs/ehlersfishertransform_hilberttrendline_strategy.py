import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'HilbertTrendline': 1.0
        })
    )
