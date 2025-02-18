import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
