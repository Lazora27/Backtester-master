import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'DonchianVolatility': 1.0
        })
    )
