import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
