import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
