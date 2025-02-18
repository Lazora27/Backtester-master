import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'DonchianVolatility': 1.0
        })
    )
