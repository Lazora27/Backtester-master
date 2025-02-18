import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'LiquidityIndex': 1.0
        })
    )
