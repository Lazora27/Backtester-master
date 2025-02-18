import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'DonchianVolatility': 1.0
        })
    )
