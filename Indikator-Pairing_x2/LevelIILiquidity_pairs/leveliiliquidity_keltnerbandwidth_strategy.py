import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
