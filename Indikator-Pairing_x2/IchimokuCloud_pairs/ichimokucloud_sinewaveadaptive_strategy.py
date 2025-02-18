import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
