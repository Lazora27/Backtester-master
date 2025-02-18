import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
