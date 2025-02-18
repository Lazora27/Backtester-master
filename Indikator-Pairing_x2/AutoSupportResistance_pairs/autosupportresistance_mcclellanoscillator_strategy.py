import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_McClellanOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und McClellanOscillator
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'McClellanOscillator': 1.0
        })
    )
