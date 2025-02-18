import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'VolumeOscillator': 1.0
        })
    )
