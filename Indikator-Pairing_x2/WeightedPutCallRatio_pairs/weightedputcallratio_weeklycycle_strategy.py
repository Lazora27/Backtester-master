import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'WeeklyCycle': 1.0
        })
    )
