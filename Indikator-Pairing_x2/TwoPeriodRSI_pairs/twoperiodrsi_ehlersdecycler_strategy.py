import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'EhlersDecycler': 1.0
        })
    )
