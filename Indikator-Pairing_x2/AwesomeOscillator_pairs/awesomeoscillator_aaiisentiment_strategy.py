import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'AAIISentiment': 1.0
        })
    )
