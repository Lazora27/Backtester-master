import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'HullMovingAverage': 1.0
        })
    )
