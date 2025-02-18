import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
