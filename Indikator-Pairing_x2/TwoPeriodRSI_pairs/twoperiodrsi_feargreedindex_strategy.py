import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'FearGreedIndex': 1.0
        })
    )
