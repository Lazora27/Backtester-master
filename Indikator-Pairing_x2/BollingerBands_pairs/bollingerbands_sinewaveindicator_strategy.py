import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
