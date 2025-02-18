import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'HilbertTrendline': 1.0
        })
    )
