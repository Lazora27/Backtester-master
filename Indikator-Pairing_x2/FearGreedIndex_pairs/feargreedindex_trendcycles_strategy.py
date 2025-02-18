import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
