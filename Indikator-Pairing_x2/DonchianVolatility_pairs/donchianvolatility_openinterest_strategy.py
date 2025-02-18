import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und OpenInterest
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'OpenInterest': 1.0
        })
    )
