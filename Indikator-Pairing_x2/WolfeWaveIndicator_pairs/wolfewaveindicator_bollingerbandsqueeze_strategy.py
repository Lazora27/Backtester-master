import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
