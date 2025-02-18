import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'VolatilityIndex': 1.0
        })
    )
