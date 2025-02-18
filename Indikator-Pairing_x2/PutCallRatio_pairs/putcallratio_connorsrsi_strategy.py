import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ConnorsRSI': 1.0
        })
    )
