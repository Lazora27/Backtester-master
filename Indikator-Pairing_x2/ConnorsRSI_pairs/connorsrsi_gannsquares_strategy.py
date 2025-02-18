import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und GannSquares
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'GannSquares': 1.0
        })
    )
