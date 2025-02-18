import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'DonchianVolatility': 1.0
        })
    )
