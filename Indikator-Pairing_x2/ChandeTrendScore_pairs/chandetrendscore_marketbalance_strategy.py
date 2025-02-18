import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'MarketBalance': 1.0
        })
    )
