import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'DonchianVolatility': 1.0
        })
    )
