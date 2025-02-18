import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
