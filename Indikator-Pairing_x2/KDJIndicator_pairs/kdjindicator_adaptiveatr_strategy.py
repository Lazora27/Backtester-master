import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'AdaptiveATR': 1.0
        })
    )
