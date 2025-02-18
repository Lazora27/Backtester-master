import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'WeightedCycle': 1.0
        })
    )
