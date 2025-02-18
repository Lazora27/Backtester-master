import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceCycleOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceCycleOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'PriceCycleOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
