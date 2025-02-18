import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'DonchianVolatility': 1.0
        })
    )
