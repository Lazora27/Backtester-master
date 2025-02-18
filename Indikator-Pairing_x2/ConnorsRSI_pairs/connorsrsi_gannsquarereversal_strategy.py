import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'GannSquareReversal': 1.0
        })
    )
