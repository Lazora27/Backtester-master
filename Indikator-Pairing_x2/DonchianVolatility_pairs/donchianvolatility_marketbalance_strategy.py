import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und MarketBalance
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'MarketBalance': 1.0
        })
    )
