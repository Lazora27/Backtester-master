import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_WyckoffWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und WyckoffWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'WyckoffWaveIndicator': {
                'class': WyckoffWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffWaveIndicator'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'WyckoffWaveIndicator': 1.0
        })
    )
