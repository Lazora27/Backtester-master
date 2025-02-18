import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_OrderFlowVolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und OrderFlowVolumeProfile
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'OrderFlowVolumeProfile': {
                'class': OrderFlowVolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowVolumeProfile'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'OrderFlowVolumeProfile': 1.0
        })
    )
