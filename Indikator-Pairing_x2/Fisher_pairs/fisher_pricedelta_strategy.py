import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und PriceDelta
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'PriceDelta': 1.0
        })
    )
