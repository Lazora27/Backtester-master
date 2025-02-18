import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
