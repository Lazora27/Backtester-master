import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
