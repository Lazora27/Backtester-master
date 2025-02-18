import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'VolumeOscillator': 1.0
        })
    )
