import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
