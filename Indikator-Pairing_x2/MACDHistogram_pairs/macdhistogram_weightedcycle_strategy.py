import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'WeightedCycle': 1.0
        })
    )
