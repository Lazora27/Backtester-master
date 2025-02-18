import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und BollingerBands
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'BollingerBands': 1.0
        })
    )
