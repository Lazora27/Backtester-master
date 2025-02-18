import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und DemandIndex
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'DemandIndex': 1.0
        })
    )
