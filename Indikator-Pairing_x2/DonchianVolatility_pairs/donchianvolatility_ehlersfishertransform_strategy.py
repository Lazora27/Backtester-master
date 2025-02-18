import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
