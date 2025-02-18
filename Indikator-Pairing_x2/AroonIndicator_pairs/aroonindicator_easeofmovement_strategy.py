import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'EaseOfMovement': 1.0
        })
    )
