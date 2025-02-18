import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
