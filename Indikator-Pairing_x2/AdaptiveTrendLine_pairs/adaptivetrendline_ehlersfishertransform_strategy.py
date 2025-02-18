import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
