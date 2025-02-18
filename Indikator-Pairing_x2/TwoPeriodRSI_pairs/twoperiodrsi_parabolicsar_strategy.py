import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'ParabolicSAR': 1.0
        })
    )
