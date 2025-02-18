import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'WeightedCycle': 1.0
        })
    )
