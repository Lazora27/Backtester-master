import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
