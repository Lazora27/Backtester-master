import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'VolatilityIndex': 1.0
        })
    )
