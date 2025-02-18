import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MomentumIndicator': 1.0
        })
    )
