import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
