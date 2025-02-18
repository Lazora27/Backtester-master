import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'EldersForceIndex': 1.0
        })
    )
