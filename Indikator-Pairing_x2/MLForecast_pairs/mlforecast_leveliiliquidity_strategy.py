import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
