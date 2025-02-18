import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
