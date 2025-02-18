import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
