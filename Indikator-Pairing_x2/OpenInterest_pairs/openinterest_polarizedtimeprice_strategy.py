import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
