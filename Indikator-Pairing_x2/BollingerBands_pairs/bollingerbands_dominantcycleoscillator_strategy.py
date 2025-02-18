import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
