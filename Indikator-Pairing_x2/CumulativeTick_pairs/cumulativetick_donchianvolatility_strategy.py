import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'DonchianVolatility': 1.0
        })
    )
