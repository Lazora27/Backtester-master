import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'BradleySiderograph': 1.0
        })
    )
