import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
