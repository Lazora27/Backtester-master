import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'LiquidityIndex': 1.0
        })
    )
