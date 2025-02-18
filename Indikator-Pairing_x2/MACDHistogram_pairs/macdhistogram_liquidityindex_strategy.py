import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'LiquidityIndex': 1.0
        })
    )
