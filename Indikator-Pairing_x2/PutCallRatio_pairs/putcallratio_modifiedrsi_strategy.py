import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ModifiedRSI': 1.0
        })
    )
