import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und GannAngles
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'GannAngles': 1.0
        })
    )
