import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'FearGreedIndex': 1.0
        })
    )
