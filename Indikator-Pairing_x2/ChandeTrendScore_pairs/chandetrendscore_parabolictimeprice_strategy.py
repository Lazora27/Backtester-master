import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
