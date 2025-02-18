import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'SmoothedCycle': 1.0
        })
    )
