import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
