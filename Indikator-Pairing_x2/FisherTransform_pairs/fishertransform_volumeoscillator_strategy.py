import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'VolumeOscillator': 1.0
        })
    )
