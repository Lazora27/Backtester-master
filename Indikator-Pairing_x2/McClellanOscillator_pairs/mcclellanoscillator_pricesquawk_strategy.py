import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'PriceSquawk': 1.0
        })
    )
