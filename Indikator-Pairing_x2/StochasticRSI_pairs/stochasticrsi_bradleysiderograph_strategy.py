import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'BradleySiderograph': 1.0
        })
    )
