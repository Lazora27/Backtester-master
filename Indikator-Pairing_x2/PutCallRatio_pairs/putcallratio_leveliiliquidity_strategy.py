import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
