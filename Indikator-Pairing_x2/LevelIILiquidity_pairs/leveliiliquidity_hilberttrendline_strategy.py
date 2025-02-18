import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'HilbertTrendline': 1.0
        })
    )
