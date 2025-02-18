import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
