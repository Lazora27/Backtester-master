import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'EaseOfMovement': 1.0
        })
    )
