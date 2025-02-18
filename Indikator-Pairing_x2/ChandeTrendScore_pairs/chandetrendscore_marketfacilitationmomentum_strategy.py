import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_MarketFacilitationMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und MarketFacilitationMomentum
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'MarketFacilitationMomentum': {
                'class': MarketFacilitationMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationMomentum'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'MarketFacilitationMomentum': 1.0
        })
    )
