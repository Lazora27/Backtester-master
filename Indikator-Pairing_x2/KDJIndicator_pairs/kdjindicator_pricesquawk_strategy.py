import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'PriceSquawk': 1.0
        })
    )
