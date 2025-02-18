import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'ParabolicSAR': 1.0
        })
    )
