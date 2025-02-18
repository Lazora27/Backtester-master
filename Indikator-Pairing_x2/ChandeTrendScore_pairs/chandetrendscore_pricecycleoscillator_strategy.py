import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
