import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
