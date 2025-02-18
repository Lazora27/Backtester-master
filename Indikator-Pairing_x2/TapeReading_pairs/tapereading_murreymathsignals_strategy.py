import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
