import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
