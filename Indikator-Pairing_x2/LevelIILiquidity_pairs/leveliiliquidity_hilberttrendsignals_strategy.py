import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
