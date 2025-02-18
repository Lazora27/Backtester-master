import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und PivotPoints
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'PivotPoints': 1.0
        })
    )
