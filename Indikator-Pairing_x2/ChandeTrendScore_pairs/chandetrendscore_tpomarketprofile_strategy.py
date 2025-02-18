import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
