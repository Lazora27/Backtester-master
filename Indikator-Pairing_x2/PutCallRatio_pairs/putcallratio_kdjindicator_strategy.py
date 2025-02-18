import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'KDJIndicator': 1.0
        })
    )
