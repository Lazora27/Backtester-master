import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MassIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MassIndex': 1.0
        })
    )
