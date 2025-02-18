import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und DemandIndex
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'DemandIndex': 1.0
        })
    )
