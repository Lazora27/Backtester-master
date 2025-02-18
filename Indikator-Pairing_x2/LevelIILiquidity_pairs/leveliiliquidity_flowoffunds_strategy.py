import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'FlowOfFunds': 1.0
        })
    )
