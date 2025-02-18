import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
