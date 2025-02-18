import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
