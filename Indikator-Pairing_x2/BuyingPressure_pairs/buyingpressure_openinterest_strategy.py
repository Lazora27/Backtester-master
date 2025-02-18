import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und OpenInterest
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'OpenInterest': 1.0
        })
    )
