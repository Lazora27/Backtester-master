import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'EhlersDecycler': 1.0
        })
    )
