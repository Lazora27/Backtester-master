import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
