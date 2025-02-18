import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'ExtensionProjections': 1.0
        })
    )
