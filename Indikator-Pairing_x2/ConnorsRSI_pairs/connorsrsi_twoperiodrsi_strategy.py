import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
