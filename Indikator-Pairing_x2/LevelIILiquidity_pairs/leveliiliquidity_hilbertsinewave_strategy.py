import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'HilbertSinewave': 1.0
        })
    )
