import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'VolumeOscillator': 1.0
        })
    )
