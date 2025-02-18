import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceCycleOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceCycleOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'PriceCycleOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
