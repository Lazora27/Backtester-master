import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'PriceSquawk': 1.0
        })
    )
