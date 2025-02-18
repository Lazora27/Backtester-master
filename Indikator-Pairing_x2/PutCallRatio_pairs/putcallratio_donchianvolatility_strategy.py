import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'DonchianVolatility': 1.0
        })
    )
