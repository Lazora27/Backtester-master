import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'EaseOfMovement': 1.0
        })
    )
