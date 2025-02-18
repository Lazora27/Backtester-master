import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
