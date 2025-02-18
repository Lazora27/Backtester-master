import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'VolumeDelta': 1.0
        })
    )
