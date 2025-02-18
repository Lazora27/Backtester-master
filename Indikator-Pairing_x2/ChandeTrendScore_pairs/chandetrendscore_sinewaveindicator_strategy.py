import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
