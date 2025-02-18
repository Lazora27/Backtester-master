import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'VolumeOscillator': 1.0
        })
    )
