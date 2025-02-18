import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'EaseOfMovement': 1.0
        })
    )
