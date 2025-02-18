import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
