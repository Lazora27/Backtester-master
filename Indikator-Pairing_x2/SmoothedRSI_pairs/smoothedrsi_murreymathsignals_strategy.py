import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
