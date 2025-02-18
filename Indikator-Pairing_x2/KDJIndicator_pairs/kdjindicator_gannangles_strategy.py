import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und GannAngles
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'GannAngles': 1.0
        })
    )
