import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
