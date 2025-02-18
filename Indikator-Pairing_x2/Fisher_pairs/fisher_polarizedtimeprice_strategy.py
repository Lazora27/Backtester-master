import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
