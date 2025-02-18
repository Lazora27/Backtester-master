import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'ParabolicSAR': 1.0
        })
    )
