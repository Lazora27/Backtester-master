import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
