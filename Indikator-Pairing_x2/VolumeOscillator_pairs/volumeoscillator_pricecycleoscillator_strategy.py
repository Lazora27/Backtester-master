import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
