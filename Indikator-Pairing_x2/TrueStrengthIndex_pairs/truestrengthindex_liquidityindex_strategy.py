import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'LiquidityIndex': 1.0
        })
    )
