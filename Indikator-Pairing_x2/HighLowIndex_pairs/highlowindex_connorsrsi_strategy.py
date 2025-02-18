import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ConnorsRSI': 1.0
        })
    )
