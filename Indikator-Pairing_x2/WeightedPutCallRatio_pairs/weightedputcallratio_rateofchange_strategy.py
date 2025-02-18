import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und RateOfChange
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'RateOfChange': 1.0
        })
    )
