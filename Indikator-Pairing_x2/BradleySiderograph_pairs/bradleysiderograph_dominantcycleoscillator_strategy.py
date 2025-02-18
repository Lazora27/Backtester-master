import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
