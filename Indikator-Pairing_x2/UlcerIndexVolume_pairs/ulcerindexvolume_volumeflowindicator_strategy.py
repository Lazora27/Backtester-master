import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
