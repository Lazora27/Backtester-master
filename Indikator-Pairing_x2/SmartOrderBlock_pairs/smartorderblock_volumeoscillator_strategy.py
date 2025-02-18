import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'VolumeOscillator': 1.0
        })
    )
