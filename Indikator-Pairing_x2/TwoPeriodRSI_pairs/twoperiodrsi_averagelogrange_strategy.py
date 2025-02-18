import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'AverageLogRange': 1.0
        })
    )
