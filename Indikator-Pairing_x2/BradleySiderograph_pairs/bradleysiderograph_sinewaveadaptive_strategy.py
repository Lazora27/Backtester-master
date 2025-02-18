import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
