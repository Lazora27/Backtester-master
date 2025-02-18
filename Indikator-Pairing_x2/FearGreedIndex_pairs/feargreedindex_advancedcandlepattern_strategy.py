import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
