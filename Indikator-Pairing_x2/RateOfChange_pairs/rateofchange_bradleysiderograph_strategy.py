import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'BradleySiderograph': 1.0
        })
    )
