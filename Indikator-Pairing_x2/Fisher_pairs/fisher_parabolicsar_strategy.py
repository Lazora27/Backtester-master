import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ParabolicSAR': 1.0
        })
    )
