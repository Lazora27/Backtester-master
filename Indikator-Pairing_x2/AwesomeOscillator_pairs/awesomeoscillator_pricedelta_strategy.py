import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und PriceDelta
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'PriceDelta': 1.0
        })
    )
