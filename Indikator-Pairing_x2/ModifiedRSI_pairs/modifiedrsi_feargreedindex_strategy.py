import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'FearGreedIndex': 1.0
        })
    )
