import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'LiquidityIndex': 1.0
        })
    )
