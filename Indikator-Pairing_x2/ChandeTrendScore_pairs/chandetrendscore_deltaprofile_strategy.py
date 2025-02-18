import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'DeltaProfile': 1.0
        })
    )
