import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
