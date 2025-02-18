import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'LiquidityIndex': 1.0
        })
    )
