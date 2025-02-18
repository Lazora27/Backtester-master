import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
