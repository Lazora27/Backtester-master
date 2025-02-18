import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'BollingerPercentB': 1.0
        })
    )
