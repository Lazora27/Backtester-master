import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
