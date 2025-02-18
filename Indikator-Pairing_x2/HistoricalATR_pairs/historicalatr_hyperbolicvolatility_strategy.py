import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
