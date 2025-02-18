import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'BradleySiderograph': 1.0
        })
    )
