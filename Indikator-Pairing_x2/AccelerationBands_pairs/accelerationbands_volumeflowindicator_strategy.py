import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
