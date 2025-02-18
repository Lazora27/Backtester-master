import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
