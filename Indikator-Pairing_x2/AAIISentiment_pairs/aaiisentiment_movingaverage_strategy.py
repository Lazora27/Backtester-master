import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und MovingAverage
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'MovingAverage': 1.0
        })
    )
