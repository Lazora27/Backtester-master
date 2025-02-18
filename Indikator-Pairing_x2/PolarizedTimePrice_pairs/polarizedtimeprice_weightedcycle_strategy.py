import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'WeightedCycle': 1.0
        })
    )
