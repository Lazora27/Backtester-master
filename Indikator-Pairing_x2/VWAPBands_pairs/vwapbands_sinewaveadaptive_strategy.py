import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
