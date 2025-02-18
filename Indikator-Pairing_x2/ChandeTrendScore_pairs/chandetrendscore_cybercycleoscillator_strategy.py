import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
