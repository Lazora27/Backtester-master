import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderFlowVolumeProfile_PolarizedFractalEfficiency_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderFlowVolumeProfile und PolarizedFractalEfficiency
    """
    
    params = (
        ('indicators', {
            'OrderFlowVolumeProfile': {
                'class': OrderFlowVolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderFlowVolumeProfile'>
            },
            'PolarizedFractalEfficiency': {
                'class': PolarizedFractalEfficiency,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedFractalEfficiency'>
            }
        }),
        ('weights', {
            'OrderFlowVolumeProfile': 1.0,
            'PolarizedFractalEfficiency': 1.0
        })
    )
