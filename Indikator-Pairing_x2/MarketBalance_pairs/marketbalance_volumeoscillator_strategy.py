import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'VolumeOscillator': 1.0
        })
    )
