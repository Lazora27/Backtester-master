import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'DonchianVolatility': 1.0
        })
    )
