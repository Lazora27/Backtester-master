import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
