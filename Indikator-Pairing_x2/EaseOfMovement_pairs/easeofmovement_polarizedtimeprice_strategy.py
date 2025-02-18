import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
