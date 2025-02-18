import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und TapeReading
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'TapeReading': 1.0
        })
    )
