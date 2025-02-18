import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'IchimokuCloud': 1.0
        })
    )
