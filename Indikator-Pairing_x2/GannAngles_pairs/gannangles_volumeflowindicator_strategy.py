import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
