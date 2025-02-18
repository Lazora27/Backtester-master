import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'AverageLogRange': 1.0
        })
    )
