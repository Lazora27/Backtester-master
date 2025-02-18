import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
