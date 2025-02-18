import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
