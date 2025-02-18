import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ConnorsRSI': 1.0
        })
    )
