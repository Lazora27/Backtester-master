import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'ConnorsRSI': 1.0
        })
    )
