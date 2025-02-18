import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'VortexIndicator': 1.0
        })
    )
