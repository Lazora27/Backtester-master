import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
