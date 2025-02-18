import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'ConnorsRSI': 1.0
        })
    )
