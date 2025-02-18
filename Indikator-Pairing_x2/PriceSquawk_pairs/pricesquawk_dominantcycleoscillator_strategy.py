import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
