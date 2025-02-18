import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
