import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
