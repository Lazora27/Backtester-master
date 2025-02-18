import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'LiquidityIndex': 1.0
        })
    )
