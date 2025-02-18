import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
