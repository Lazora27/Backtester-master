import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
