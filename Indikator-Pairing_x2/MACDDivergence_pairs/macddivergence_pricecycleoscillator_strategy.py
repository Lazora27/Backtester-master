import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
