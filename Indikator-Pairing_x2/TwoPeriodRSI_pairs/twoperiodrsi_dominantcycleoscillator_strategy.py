import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
