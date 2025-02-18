import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'ParabolicSAR': 1.0
        })
    )
