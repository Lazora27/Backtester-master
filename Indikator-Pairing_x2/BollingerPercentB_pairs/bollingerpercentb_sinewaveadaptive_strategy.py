import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
