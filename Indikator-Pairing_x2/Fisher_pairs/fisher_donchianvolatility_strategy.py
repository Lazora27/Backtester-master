import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'DonchianVolatility': 1.0
        })
    )
