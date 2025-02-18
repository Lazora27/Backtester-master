import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'TRIXIndicator': 1.0
        })
    )
