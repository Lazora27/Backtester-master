import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
