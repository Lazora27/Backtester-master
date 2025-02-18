import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'EaseOfMovement': 1.0
        })
    )
