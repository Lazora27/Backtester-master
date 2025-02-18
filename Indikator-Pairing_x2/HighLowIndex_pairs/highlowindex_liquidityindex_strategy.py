import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'LiquidityIndex': 1.0
        })
    )
