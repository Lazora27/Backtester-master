import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'ConnorsRSI': 1.0
        })
    )
