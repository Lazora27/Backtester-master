import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und PriceDelta
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'PriceDelta': 1.0
        })
    )
