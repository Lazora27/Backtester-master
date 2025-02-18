import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
