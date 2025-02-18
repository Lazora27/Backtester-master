import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'AroonIndicator': 1.0
        })
    )
