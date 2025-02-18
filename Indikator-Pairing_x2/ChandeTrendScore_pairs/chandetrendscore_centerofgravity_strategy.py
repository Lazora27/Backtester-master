import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'CenterOfGravity': 1.0
        })
    )
