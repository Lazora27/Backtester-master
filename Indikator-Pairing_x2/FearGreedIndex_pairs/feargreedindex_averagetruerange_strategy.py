import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
