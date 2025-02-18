import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'ForecastOscillator': 1.0
        })
    )
