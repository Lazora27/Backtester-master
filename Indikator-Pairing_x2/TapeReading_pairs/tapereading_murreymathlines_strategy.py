import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'MurreyMathLines': 1.0
        })
    )
