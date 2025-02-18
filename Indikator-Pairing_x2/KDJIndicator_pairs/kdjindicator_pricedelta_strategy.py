import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und PriceDelta
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'PriceDelta': 1.0
        })
    )
