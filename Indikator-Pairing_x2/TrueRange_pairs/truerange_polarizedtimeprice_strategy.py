import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
