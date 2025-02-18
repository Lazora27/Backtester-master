import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'WeightedCycle': 1.0
        })
    )
