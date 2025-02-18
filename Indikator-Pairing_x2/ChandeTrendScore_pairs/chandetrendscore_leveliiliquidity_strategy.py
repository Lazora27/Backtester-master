import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
