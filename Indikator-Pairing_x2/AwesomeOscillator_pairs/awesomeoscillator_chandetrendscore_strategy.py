import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
