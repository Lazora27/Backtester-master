import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
