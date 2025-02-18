import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
