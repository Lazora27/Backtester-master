import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
