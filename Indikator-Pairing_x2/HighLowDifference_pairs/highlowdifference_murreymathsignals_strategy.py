import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
