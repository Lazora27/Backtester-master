import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
