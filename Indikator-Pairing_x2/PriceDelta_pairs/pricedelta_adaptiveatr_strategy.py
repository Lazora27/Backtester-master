import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'AdaptiveATR': 1.0
        })
    )
