import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'WeightedCycle': 1.0
        })
    )
