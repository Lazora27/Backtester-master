import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
