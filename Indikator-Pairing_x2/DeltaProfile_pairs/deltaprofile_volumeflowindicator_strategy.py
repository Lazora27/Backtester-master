import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
