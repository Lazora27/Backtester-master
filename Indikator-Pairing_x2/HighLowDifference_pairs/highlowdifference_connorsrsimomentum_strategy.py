import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ConnorsRSIMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ConnorsRSIMomentum
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ConnorsRSIMomentum': {
                'class': ConnorsRSIMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSIMomentum'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ConnorsRSIMomentum': 1.0
        })
    )
