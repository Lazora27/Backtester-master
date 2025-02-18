import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'ParabolicSAR': 1.0
        })
    )
