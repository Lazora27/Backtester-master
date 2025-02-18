import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
