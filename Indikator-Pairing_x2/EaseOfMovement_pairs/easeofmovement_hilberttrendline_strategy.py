import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'HilbertTrendline': 1.0
        })
    )
