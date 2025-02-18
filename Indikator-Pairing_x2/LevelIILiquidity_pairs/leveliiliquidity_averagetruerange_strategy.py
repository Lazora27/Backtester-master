import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'AverageTrueRange': 1.0
        })
    )
