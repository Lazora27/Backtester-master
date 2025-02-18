import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'SeasonalStrength': 1.0
        })
    )
