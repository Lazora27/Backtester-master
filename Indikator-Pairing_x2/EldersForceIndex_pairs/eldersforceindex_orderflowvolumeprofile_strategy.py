import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_OrderFlowVolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und OrderFlowVolumeProfile
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'OrderFlowVolumeProfile': {
                'class': OrderFlowVolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowVolumeProfile'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'OrderFlowVolumeProfile': 1.0
        })
    )
