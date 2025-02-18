import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
