import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
