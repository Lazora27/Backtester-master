import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'UlcerIndex': 1.0
        })
    )
