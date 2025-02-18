import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
