import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
