import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'HistoricalATR': 1.0
        })
    )
