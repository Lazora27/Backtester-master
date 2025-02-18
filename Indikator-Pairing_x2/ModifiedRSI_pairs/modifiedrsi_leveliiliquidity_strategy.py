import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
