import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
