import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'BuyingPressure': 1.0
        })
    )
