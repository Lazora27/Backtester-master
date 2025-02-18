import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'VortexIndicator': 1.0
        })
    )
