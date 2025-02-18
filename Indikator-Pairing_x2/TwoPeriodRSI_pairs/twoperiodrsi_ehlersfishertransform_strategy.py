import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
