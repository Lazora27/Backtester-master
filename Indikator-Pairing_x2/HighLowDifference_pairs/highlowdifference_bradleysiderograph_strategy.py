import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'BradleySiderograph': 1.0
        })
    )
