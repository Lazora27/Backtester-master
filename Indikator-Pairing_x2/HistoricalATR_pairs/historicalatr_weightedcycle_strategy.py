import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'WeightedCycle': 1.0
        })
    )
