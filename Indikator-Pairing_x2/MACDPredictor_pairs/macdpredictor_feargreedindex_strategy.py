import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'FearGreedIndex': 1.0
        })
    )
