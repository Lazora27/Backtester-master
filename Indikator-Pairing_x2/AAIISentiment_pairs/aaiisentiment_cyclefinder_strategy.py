import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'CycleFinder': 1.0
        })
    )
