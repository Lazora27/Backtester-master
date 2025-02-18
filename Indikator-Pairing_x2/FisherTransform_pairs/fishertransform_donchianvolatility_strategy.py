import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'DonchianVolatility': 1.0
        })
    )
