import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'BuyingPressure': 1.0
        })
    )
