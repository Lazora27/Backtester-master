import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'BradleySiderograph': 1.0
        })
    )
