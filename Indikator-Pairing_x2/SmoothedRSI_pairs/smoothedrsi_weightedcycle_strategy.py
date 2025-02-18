import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'WeightedCycle': 1.0
        })
    )
