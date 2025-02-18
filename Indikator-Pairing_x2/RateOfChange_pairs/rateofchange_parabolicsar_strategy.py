import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'ParabolicSAR': 1.0
        })
    )
