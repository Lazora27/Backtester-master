import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
