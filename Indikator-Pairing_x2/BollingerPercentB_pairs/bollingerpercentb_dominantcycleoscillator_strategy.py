import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
