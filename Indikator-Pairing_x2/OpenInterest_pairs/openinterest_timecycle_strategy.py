import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und TimeCycle
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'TimeCycle': 1.0
        })
    )
