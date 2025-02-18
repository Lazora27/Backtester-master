import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
