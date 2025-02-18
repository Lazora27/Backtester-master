import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'BradleySiderograph': 1.0
        })
    )
