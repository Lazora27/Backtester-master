import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'LiquidityIndex': 1.0
        })
    )
