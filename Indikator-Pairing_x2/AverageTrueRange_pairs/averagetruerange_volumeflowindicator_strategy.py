import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
