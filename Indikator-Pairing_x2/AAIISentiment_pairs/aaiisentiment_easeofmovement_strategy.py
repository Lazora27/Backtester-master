import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'EaseOfMovement': 1.0
        })
    )
