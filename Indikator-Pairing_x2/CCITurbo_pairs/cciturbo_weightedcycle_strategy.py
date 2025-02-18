import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'WeightedCycle': 1.0
        })
    )
