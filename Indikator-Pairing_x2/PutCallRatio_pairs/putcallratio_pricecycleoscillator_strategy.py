import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
