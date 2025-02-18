import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
