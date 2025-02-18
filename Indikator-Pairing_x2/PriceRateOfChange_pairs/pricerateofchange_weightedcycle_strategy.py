import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'WeightedCycle': 1.0
        })
    )
