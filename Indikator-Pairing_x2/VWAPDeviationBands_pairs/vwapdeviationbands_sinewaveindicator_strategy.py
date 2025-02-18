import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
