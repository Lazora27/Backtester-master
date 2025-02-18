import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
