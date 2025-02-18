import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
