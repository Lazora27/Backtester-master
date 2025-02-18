import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
