import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
