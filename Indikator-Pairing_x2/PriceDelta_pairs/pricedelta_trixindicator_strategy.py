import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'TRIXIndicator': 1.0
        })
    )
