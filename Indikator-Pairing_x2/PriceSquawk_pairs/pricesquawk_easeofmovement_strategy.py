import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'EaseOfMovement': 1.0
        })
    )
