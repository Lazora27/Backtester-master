import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
