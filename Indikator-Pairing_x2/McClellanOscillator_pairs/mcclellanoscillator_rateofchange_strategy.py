import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und RateOfChange
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'RateOfChange': 1.0
        })
    )
