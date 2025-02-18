import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und RateOfChange
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'RateOfChange': 1.0
        })
    )
