import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
