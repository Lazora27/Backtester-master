import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
