import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_PercentageVolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und PercentageVolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'PercentageVolumeOscillator': {
                'class': PercentageVolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentageVolumeOscillator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'PercentageVolumeOscillator': 1.0
        })
    )
