import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'BradleySiderograph': 1.0
        })
    )
