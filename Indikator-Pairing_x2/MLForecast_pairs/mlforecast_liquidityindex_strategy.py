import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'LiquidityIndex': 1.0
        })
    )
