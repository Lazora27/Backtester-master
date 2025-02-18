import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
