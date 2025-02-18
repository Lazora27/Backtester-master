import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'BuyingPressure': 1.0
        })
    )
