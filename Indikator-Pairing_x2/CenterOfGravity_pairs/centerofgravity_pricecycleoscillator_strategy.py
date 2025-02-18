import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
