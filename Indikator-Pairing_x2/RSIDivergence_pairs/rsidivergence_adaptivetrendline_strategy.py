import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
