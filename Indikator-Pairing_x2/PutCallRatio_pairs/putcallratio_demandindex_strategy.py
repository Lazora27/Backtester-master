import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und DemandIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'DemandIndex': 1.0
        })
    )
