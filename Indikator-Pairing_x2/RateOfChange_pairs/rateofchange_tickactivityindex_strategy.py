import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'TickActivityIndex': 1.0
        })
    )
