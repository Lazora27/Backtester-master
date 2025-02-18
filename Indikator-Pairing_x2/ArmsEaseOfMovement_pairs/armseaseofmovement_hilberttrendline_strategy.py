import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsEaseOfMovement_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsEaseOfMovement und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ArmsEaseOfMovement': {
                'class': ArmsEaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsEaseOfMovement'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ArmsEaseOfMovement': 1.0,
            'HilbertTrendline': 1.0
        })
    )
