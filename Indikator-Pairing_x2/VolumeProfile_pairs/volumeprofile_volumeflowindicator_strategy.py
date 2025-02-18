import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
