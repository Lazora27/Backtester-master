import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TimeCycle
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TimeCycle': 1.0
        })
    )
