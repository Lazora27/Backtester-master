import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
