import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'LiquidityIndex': 1.0
        })
    )
