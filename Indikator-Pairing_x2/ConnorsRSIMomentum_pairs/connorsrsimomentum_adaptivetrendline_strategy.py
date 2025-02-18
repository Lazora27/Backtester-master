import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSIMomentum_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSIMomentum und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'ConnorsRSIMomentum': {
                'class': ConnorsRSIMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSIMomentum'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'ConnorsRSIMomentum': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
