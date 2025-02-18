import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'DonchianVolatility': 1.0
        })
    )
