import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'HilbertTrendline': 1.0
        })
    )
