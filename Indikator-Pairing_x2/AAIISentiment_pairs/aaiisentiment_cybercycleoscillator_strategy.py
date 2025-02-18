import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
