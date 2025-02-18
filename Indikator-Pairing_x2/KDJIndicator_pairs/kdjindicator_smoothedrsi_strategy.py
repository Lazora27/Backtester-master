import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'SmoothedRSI': 1.0
        })
    )
