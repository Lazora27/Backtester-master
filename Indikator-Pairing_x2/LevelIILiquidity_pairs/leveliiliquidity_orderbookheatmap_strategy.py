import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
