import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
