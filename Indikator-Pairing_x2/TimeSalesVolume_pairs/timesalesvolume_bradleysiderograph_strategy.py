import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'BradleySiderograph': 1.0
        })
    )
