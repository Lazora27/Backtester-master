import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'DonchianVolatility': 1.0
        })
    )
